from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard = [ 
        [
            KeyboardButton(text='Меню на сегодня'),
        ],
        [
            KeyboardButton(text='Список мероприятий'),
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
            KeyboardButton(text='Звукари')
        ],
        [
            KeyboardButton(text='Видеографы')
        ],
        [
            KeyboardButton(text='<<<')
        ]
    ],
    resize_keyboard=True
)






