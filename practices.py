# -*- coding: utf-8 -*-
"""
Данные о категориях и аудиопрактиках.

Структура:
CATEGORIES = {
    "category_id": {
        "title": "Название категории",
        "emoji": "эмодзи для кнопки",
        "practices": {
            "practice_id": {
                "title": "Название практики",
                "description": "Короткое описание",
                "duration": "10 мин",
                "file": "имя_файла.mp3",  # должен лежать в папке audio/
            },
            ...
        }
    },
    ...
}

Чтобы добавить свои аудио: положите mp3/ogg файл в папку audio/ с именем,
указанным в поле "file". Пока файла нет — бот вместо аудио пришлёт
текстовое описание практики с пометкой "аудио скоро появится".
"""

CATEGORIES = {
    "sleep": {
        "title": "Сон",
        "emoji": "🌙",
        "practices": {
            "sleep_01": {
                "title": "Глубокий сон",
                "description": "Плавное расслабление тела и дыхания, чтобы легко погрузиться в сон.",
                "duration": "15 мин",
                "file": "sleep_01.mp3",
            },
            "sleep_02": {
                "title": "Расслабление перед сном",
                "description": "Снимаем напряжение дня и готовим ум к отдыху.",
                "duration": "10 мин",
                "file": "sleep_02.mp3",
            },
            "sleep_03": {
                "title": "Успокаивающее дыхание",
                "description": "Медленное дыхание для замедления пульса и мыслей перед сном.",
                "duration": "8 мин",
                "file": "sleep_03.mp3",
            },
            "sleep_04": {
                "title": "Тело в покое",
                "description": "Сканирование тела от макушки до пяток — практика для глубокого расслабления.",
                "duration": "12 мин",
                "file": "sleep_04.mp3",
            },
            "sleep_05": {
                "title": "Тихая гавань",
                "description": "Визуализация спокойного места, помогающая отпустить тревожные мысли.",
                "duration": "10 мин",
                "file": "sleep_05.mp3",
            },
        },
    },
    "stress": {
        "title": "Стресс и тревога",
        "emoji": "🌿",
        "practices": {
            "stress_01": {
                "title": "Дыхание 4-7-8",
                "description": "Простая дыхательная техника для быстрого снижения тревожности.",
                "duration": "5 мин",
                "file": "stress_01.mp3",
            },
            "stress_02": {
                "title": "Снятие напряжения",
                "description": "Прогрессивная мышечная релаксация для тела, зажатого стрессом.",
                "duration": "12 мин",
                "file": "stress_02.mp3",
            },
            "stress_03": {
                "title": "Заземление",
                "description": "Практика возвращения в момент «здесь и сейчас» через ощущения тела.",
                "duration": "7 мин",
                "file": "stress_03.mp3",
            },
            "stress_04": {
                "title": "Спокойный ум",
                "description": "Медитация для успокоения потока мыслей в тревожные моменты.",
                "duration": "10 мин",
                "file": "stress_04.mp3",
            },
            "stress_05": {
                "title": "Отпустить тревогу",
                "description": "Мягкая практика принятия и отпускания беспокоящих мыслей.",
                "duration": "9 мин",
                "file": "stress_05.mp3",
            },
        },
    },
    "focus": {
        "title": "Фокус и продуктивность",
        "emoji": "🎯",
        "practices": {
            "focus_01": {
                "title": "Утренняя концентрация",
                "description": "Настройка ума на продуктивный день с самого утра.",
                "duration": "8 мин",
                "file": "focus_01.mp3",
            },
            "focus_02": {
                "title": "Ясность ума",
                "description": "Практика для избавления от умственного шума перед важной задачей.",
                "duration": "10 мин",
                "file": "focus_02.mp3",
            },
            "focus_03": {
                "title": "Пауза для перезагрузки",
                "description": "Короткая пауза между задачами, чтобы восстановить внимание.",
                "duration": "5 мин",
                "file": "focus_03.mp3",
            },
            "focus_04": {
                "title": "Глубокая работа",
                "description": "Настройка на состояние глубокой концентрации перед важной работой.",
                "duration": "10 мин",
                "file": "focus_04.mp3",
            },
            "focus_05": {
                "title": "Возврат в момент",
                "description": "Быстрая практика внимательности при рассеянности.",
                "duration": "6 мин",
                "file": "focus_05.mp3",
            },
        },
    },
    "energy": {
        "title": "Энергия и бодрость",
        "emoji": "☀️",
        "practices": {
            "energy_01": {
                "title": "Утренняя зарядка для ума",
                "description": "Мягкое пробуждение сознания и тела в начале дня.",
                "duration": "7 мин",
                "file": "energy_01.mp3",
            },
            "energy_02": {
                "title": "Дыхание энергии",
                "description": "Активирующая дыхательная практика для прилива бодрости.",
                "duration": "6 мин",
                "file": "energy_02.mp3",
            },
            "energy_03": {
                "title": "Пробуждение тела",
                "description": "Лёгкая практика осознанности тела для снятия сонливости.",
                "duration": "8 мин",
                "file": "energy_03.mp3",
            },
            "energy_04": {
                "title": "Заряд бодрости",
                "description": "Динамичная практика для восстановления энергии в середине дня.",
                "duration": "9 мин",
                "file": "energy_04.mp3",
            },
            "energy_05": {
                "title": "Позитивный настрой",
                "description": "Практика с элементами благодарности для поднятия настроения.",
                "duration": "7 мин",
                "file": "energy_05.mp3",
            },
        },
    },
}


def get_practice(category_id: str, practice_id: str):
    """Вернуть данные практики или None."""
    category = CATEGORIES.get(category_id)
    if not category:
        return None
    return category["practices"].get(practice_id)


def total_practices_count() -> int:
    return sum(len(cat["practices"]) for cat in CATEGORIES.values())
