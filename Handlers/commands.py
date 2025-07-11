
from aiogram.types import Message
from aiogram import Router
from aiogram.filters import CommandStart
from Kbds import layout

user_router = Router()

@user_router.message(CommandStart())
async def Start_message(message: Message):
    await message.answer(
        "Ну привет ебанный рот", 
        reply_markup = layout.main_kb
        )

@user_router.message(lambda message: message.text == 'Меню на сегодня')
async def Menu_message(message: Message):
    await message.answer(
        "Вот тебе харчевня на сегодня"
        )

@user_router.message(lambda message: message.text == 'Список мероприятий')
async def list_events(message: Message):
    await message.answer(
        "Список мероприятий"
        )

@user_router.message(lambda message: message.text == 'Список Комс-Отряда')
async def list_coms_reply(message: Message):
    await message.answer(
        "Выбери группу", 
        reply_markup = layout.group_choice_kb
        )

@user_router.message(lambda message: message.text == 'FAQ')
async def questions_message(message: Message):
    await message.answer(
        "Какие-то вопросики ?" 
        )

@user_router.message(lambda message: message.text == '<<<')
async def back_to_main(message: Message):
    await message.reply(
        text = 'Заходи если что',
        reply_markup = layout.main_kb
        )

@user_router.message(lambda message: message.text == '<')
async def back_to_main(message: Message):
    await message.reply(
        text = 'Заходи если что',
        reply_markup = layout.group_choice_kb
        )

