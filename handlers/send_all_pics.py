from aiogram import Router
from aiogram.types import Message

from create_bot import news_channel_id, bot

phto_router = Router()

all_pics_name = {
    'Командир КО-25': 19,
    'Соня Пешкова': 20,
    'Богдан Огай': 40,
    'Александра Кучина': 29,
    'Артем Бахеткин': 30,
    'Макс Рябов': 31,
    'Арина Лукьянова': 32,
    'Екатерина Кожевникова': 21,
    'Ангелина Мустакова': 22,
    'Алина Беляева': 23,
    'Анастасия Левашенко': 25,
    'Елизавета Саранцева': 24,
    'Майя Подъячева': 26,
    'Александр Куулар': 33,
    'Станислав Конорев': 34,
    'Егор Десяткин': 35,
    'Алексей Малков': 39,
    'Варвара Медведева': 36,
    'Алексей Деревцов': 37,
    'Владимир Гильманов': 38,
    'Звукарь': 27,
    'Видеограф': 28
}

@phto_router.message(lambda message: message.text in all_pics_name.keys())
async def send_pics(message: Message):
    await bot.forward_message(
        chat_id = message.chat.id,
        from_chat_id = news_channel_id,
        message_id = all_pics_name[message.text]
    )
