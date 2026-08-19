# -*- coding: utf-8 -*-
"""
Telegram-бот с аудиопрактиками.

Пользователь выбирает категорию, затем практику внутри неё, и получает
аудиофайл с короткой практикой. Если аудиофайл ещё не добавлен в папку
audio/, бот присылает описание практики и предупреждает, что аудио скоро
появится — это позволяет тестировать бота ещё до того, как все записи
будут готовы.

Бот умеет работать в двух режимах, без каких-либо изменений в коде:

* Polling (для локального запуска на своём компьютере) — используется,
  если не заданы переменные окружения PORT и RENDER_EXTERNAL_URL/WEBHOOK_URL.
* Webhook (для хостинга, например Render) — включается автоматически,
  если хостинг задаёт переменную PORT (так делает Render и большинство
  PaaS-платформ) и известен внешний адрес сервиса.

Запуск локально:
    1) pip install -r requirements.txt
    2) создать .env на основе .env.example и вписать токен бота
    3) python bot.py
"""

import asyncio
import logging
import os
from pathlib import Path

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart
from aiogram.types import (
    CallbackQuery,
    FSInputFile,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from dotenv import load_dotenv

from practices import CATEGORIES, get_practice, total_practices_count

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
AUDIO_DIR = Path(__file__).parent / "audio"
WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = Router()


# ---------- Клавиатуры ----------

def categories_keyboard() -> InlineKeyboardMarkup:
    buttons = []
    for cat_id, cat in CATEGORIES.items():
        text = f"{cat['emoji']} {cat['title']}"
        buttons.append(
            [InlineKeyboardButton(text=text, callback_data=f"cat:{cat_id}")]
        )
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def practices_keyboard(category_id: str) -> InlineKeyboardMarkup:
    category = CATEGORIES[category_id]
    buttons = []
    for pr_id, practice in category["practices"].items():
        text = f"{practice['title']} · {practice['duration']}"
        buttons.append(
            [InlineKeyboardButton(text=text, callback_data=f"pr:{category_id}:{pr_id}")]
        )
    buttons.append(
        [InlineKeyboardButton(text="⬅️ Все категории", callback_data="back:categories")]
    )
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def practice_view_keyboard(category_id: str) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="⬅️ К практикам категории", callback_data=f"cat:{category_id}")],
        [InlineKeyboardButton(text="🏠 Все категории", callback_data="back:categories")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


# ---------- Хендлеры ----------

@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    count = total_practices_count()
    text = (
        "Привет! 👋\n\n"
        f"Здесь собрано {count} аудиопрактик — для сна, снятия стресса, "
        "фокуса и бодрости.\n\n"
        "Выбери категорию, чтобы увидеть практики внутри неё:"
    )
    await message.answer(text, reply_markup=categories_keyboard())


@router.message(F.text == "/practices")
async def cmd_practices(message: Message) -> None:
    await cmd_start(message)


@router.callback_query(F.data == "back:categories")
async def show_categories(callback: CallbackQuery) -> None:
    # Отправляем новое сообщение, а не редактируем предыдущее: предыдущим
    # сообщением может быть аудио с подписью, у которого нет текста для
    # edit_text (это вызвало бы ошибку Telegram API).
    await callback.message.answer(
        "Выбери категорию:",
        reply_markup=categories_keyboard(),
    )
    await callback.answer()


@router.callback_query(F.data.startswith("cat:"))
async def show_category(callback: CallbackQuery) -> None:
    category_id = callback.data.split(":", 1)[1]
    category = CATEGORIES.get(category_id)
    if not category:
        await callback.answer("Категория не найдена", show_alert=True)
        return

    text = f"{category['emoji']} {category['title']}\n\nВыбери практику:"
    await callback.message.answer(text, reply_markup=practices_keyboard(category_id))
    await callback.answer()


@router.callback_query(F.data.startswith("pr:"))
async def show_practice(callback: CallbackQuery) -> None:
    _, category_id, practice_id = callback.data.split(":", 2)
    practice = get_practice(category_id, practice_id)
    if not practice:
        await callback.answer("Практика не найдена", show_alert=True)
        return

    caption = f"🎧 {practice['title']} · {practice['duration']}\n\n{practice['description']}"
    audio_path = AUDIO_DIR / practice["file"]

    await callback.answer()

    if audio_path.exists():
        await callback.message.answer_audio(
            audio=FSInputFile(audio_path),
            caption=caption,
            reply_markup=practice_view_keyboard(category_id),
        )
    else:
        # Аудиофайл ещё не добавлен — присылаем описание и предупреждение.
        text = (
            f"{caption}\n\n"
            "⏳ Аудиозапись для этой практики скоро появится. "
            "Загляните позже!"
        )
        await callback.message.answer(text, reply_markup=practice_view_keyboard(category_id))


async def run_polling(bot: Bot, dp: Dispatcher) -> None:
    logger.info(
        "Бот запущен в режиме polling. Практик в базе: %s",
        total_practices_count(),
    )
    await dp.start_polling(bot)


def run_webhook(bot: Bot, dp: Dispatcher, base_url: str, port: int) -> None:
    async def on_startup(app: web.Application) -> None:
        webhook_url = f"{base_url}{WEBHOOK_PATH}"
        await bot.set_webhook(webhook_url)
        logger.info(
            "Бот запущен в режиме webhook (%s). Практик в базе: %s",
            webhook_url,
            total_practices_count(),
        )

    async def on_shutdown(app: web.Application) -> None:
        await bot.delete_webhook()

    async def health(request: web.Request) -> web.Response:
        # Простой ответ для проверок доступности хостингом.
        return web.Response(text="OK")

    app = web.Application()
    app.router.add_get("/", health)
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    web.run_app(app, host="0.0.0.0", port=port)


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError(
            "Не найден BOT_TOKEN. Создайте файл .env на основе .env.example "
            "и укажите там токен, полученный у @BotFather."
        )

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    port = os.getenv("PORT")
    base_url = os.getenv("RENDER_EXTERNAL_URL") or os.getenv("WEBHOOK_URL")

    if port and base_url:
        run_webhook(bot, dp, base_url.rstrip("/"), int(port))
    else:
        asyncio.run(run_polling(bot, dp))


if __name__ == "__main__":
    main()
