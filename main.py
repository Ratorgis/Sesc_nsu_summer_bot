import asyncio
import os

from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from Handlers.commands import user_router
from Handlers.commands_privat import user_router_coms

commands = ['Меню на сегодня', 'Список мероприятий', 'Список Комс-Отряда', 'FAQ', '<<<', '/start', 'Физорги', 'Макс Рябов', '<']

# bote initialization + taking token
load_dotenv(find_dotenv())
dp = Dispatcher()
bot = Bot(token = os.getenv('Token'))


@dp.message(lambda message: not(message.text in commands))
async def first_back(message: Message):
    await message.answer(
        "хуйню не пиши, кнопки бота используй"
        )

dp.include_router(user_router)
dp.include_router(user_router_coms)

# run main function 
async def main():
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)

asyncio.run(main())






