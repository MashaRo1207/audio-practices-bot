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
    "self_esteem": {
        "title": "Самооценка и принятие себя",
        "emoji": "💛",
        "practices": {
            "self_esteem_01": {
                "title": "Не только мама",
                "description": "Практика для возвращения к своей личности за пределами роли мамы.",
                "duration": "6 мин",
                "file": "self_esteem_01.mp3",
            },
            "self_esteem_02": {
                "title": "Принятие материнства",
                "description": "Мягкое принятие своего нового опыта и себя в роли мамы.",
                "duration": "5 мин",
                "file": "self_esteem_02.mp3",
            },
            "self_esteem_03": {
                "title": "Я не обязана быть идеальной",
                "description": "Практика для отпускания перфекционизма и завышенных ожиданий к себе.",
                "duration": "6 мин",
                "file": "self_esteem_03.mp3",
            },
            "self_esteem_04": {
                "title": "Я справляюсь",
                "description": "Поддерживающая практика в моменты сомнений в своих силах.",
                "duration": "5 мин",
                "file": "self_esteem_04.mp3",
            },
            "self_esteem_05": {
                "title": "Материнство без сравнения",
                "description": "Практика для освобождения от сравнения себя с другими мамами.",
                "duration": "9 мин",
                "file": "self_esteem_05.mp3",
            },
            "self_esteem_06": {
                "title": "Возвращение к себе",
                "description": "Практика для контакта с собой вне ролей и задач.",
                "duration": "8 мин",
                "file": "self_esteem_06.mp3",
            },
        },
    },
    "resource": {
        "title": "Ресурс и восстановление",
        "emoji": "🌿",
        "practices": {
            "resource_01": {
                "title": "Восстановление ресурса",
                "description": "Практика для наполнения внутренних сил, когда чувствуешь опустошение.",
                "duration": "16 мин",
                "file": "восстановление ресурса (Vocals) 3.mp3",
            },
            "resource_02": {
                "title": "Можно быть уставшей",
                "description": "Практика принятия усталости без чувства вины.",
                "duration": "8 мин",
                "file": "resource_02.mp3",
            },
            "resource_03": {
                "title": "Утро мамы",
                "description": "Короткая практика для мягкого и осознанного начала дня.",
                "duration": "7 мин",
                "file": "resource_03.mp3",
            },
            "resource_04": {
                "title": "Вечерняя практика",
                "description": "Практика для завершения дня и снятия накопленного напряжения.",
                "duration": "9 мин",
                "file": "resource_04.mp3",
            },
            "resource_05": {
                "title": "Переход от работы к материнству",
                "description": "Практика для переключения между ролями и снижения внутреннего напряжения.",
                "duration": "8 мин",
                "file": "resource_05.mp3",
            },
            "resource_06": {
                "title": "Маленькая пауза на 3 минуты",
                "description": "Сверхкороткая практика для восстановления посреди дня.",
                "duration": "3 мин",
                "file": "resource_06.mp3",
            },
            "resource_07": {
                "title": "Практика перед сном ребёнка",
                "description": "Практика для успокоения, пока ребёнок засыпает.",
                "duration": "9 мин",
                "file": "resource_07.mp3",
            },
        },
    },
    "emotions": {
        "title": "Эмоции и чувства",
        "emoji": "🌊",
        "practices": {
            "emotions_01": {
                "title": "Снятие чувства вины",
                "description": "Практика для работы с материнским чувством вины.",
                "duration": "9 мин",
                "file": "emotions_01.mp3",
            },
            "emotions_02": {
                "title": "Материнская злость",
                "description": "Практика для проживания и принятия раздражения и злости.",
                "duration": "8 мин",
                "file": "материнская злость.mp3",
            },
            "emotions_03": {
                "title": "Страх за ребёнка",
                "description": "Практика для успокоения тревожных мыслей о ребёнке.",
                "duration": "7 мин",
                "file": "страх за ребенка.mp3",
            },
            "emotions_05": {
                "title": "Скорая помощь при сильной тревоге",
                "description": "Короткая практика для момента острой паники — можно делать стоя, на ходу, с открытыми глазами.",
                "duration": "2 мин",
                "file": "emotions_05.mp3",
            },
            "emotions_04": {
                "title": "Разлука с ребёнком",
                "description": "Практика для проживания непростых чувств при расставании с ребёнком.",
                "duration": "9 мин",
                "file": "emotions_04.mp3",
            },
        },
    },
    "bond": {
        "title": "Связь с ребёнком",
        "emoji": "🤍",
        "practices": {
            "bond_01": {
                "title": "Связь с ребёнком",
                "description": "Практика для укрепления эмоциональной близости с ребёнком.",
                "duration": "6 мин",
                "file": "bond_01.mp3",
            },
            "bond_02": {
                "title": "Практика благодарности ребёнку",
                "description": "Практика для наполнения теплом и благодарностью в отношениях с ребёнком.",
                "duration": "7 мин",
                "file": "благодарность.mp3",
            },
        },
    },
    "relationships": {
        "title": "Отношения и личные границы",
        "emoji": "🧭",
        "practices": {
            "relationships_01": {
                "title": "Отношения с собственной мамой",
                "description": "Практика для работы с чувствами к своей маме.",
                "duration": "10 мин",
                "file": "relationships_01.mp3",
            },
            "relationships_02": {
                "title": "Практика для мамы нескольких детей",
                "description": "Практика поддержки для мам, воспитывающих больше одного ребёнка.",
                "duration": "9 мин",
                "file": "relationships_02.mp3",
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
