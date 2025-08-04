from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

main_kb = ReplyKeyboardMarkup(
    keyboard = [ 
        [
            KeyboardButton(text='Меню'),
        ],
        [
            KeyboardButton(text='Мероприятия'),
        ],
        [
            KeyboardButton(text='Список Комс-Отряда')
        ],
        [
            KeyboardButton(text='FAQ')
        ]
    ],
    resize_keyboard=True
)

admin_main_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = 'Меню'), KeyboardButton(text = 'Update_menu')
        ],
        [
            KeyboardButton(text = 'Мероприятия'), KeyboardButton(text = 'Update_events')
        ],
        [
            KeyboardButton(text = 'Список Комс-Отряда')
        ],
        [
            KeyboardButton(text = 'FAQ')
        ],
    ],
    resize_keyboard = True
)


group_choice_kb = ReplyKeyboardMarkup(
    keyboard = [ 
        [
            KeyboardButton(text='Командир КО-25'),
        ],
        [
            KeyboardButton(text='Культорги'),
        ],
        [
            KeyboardButton(text='Художники')
        ],
        [
            KeyboardButton(text='Физорги')
        ],
        [
            KeyboardButton(text='Поворята')
        ],
        [
            KeyboardButton(text='Звукарь')
        ],
        [
            KeyboardButton(text='Видеограф')
        ],
        [
            KeyboardButton(text='< Главное Меню')
        ]
    ],
    resize_keyboard=True
)

