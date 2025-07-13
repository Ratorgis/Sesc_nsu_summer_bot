from aiogram.types import Message
from aiogram import Router
from aiogram.filters import CommandStart
from Keybords import layout
from Sesc_nsu_summer_bot.data import data_about_users

# id: [kbds_layout, Name, Last_name, class, Room_in_dorm]

user_router = Router()

@user_router.message(CommandStart())
async def Start_message(message: Message):
    id = message.from_user.id 
    if id not in data_about_users:
        data_about_users[id] = ['main_kb', '', '', '', '']
    else:
        data_about_users[id][0] = 'main_kb'
    await message.answer(
        "Рад приветстовать тебя", 
        reply_markup = layout.main_kb
        )

@user_router.message(lambda message: message.text == 'Меню на сегодня')
async def Menu_message(message: Message):
    await message.answer(
        "Меню на сегодня"
        )

@user_router.message(lambda message: message.text == 'Список мероприятий')
async def list_events(message: Message):
    await message.answer(
        "Список мероприятий"
        )

@user_router.message(lambda message: message.text == 'Список Комс-Отряда')
async def list_coms_reply(message: Message):
    id = message.from_user.id
    if id not in data_about_users:
        data_about_users[id] = ['group_choice_kb', '', '', '', '']
    else:
        data_about_users[id][0] = 'group_choice_kb'
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
    id = message.from_user.id
    if data_about_users[id][0] == 'group_choice_kb':
        await message.reply(
            text='1',
            reply_markup = layout.main_kb
        )
    else:
        await message.reply(
            text='2',
            reply_markup = layout.group_choice_kb
        )


