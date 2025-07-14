from aiogram.types import Message
from aiogram import Router
from keyboards import koms_layout
from data import data_about_users

user_router_coms = Router()

@user_router_coms.message(lambda message: message.text == 'Физорги')
async def command_KO(message: Message):
    id = message.from_user.id 
    if id not in data_about_users:
        data_about_users[id] = ['phys_kb', '', '', '', '']
    else:
        data_about_users[id][0] = 'phys_kb'
    await message.reply(
        text='Физорги КО-25',
        reply_markup = koms_layout.phys_kb 
    )

@user_router_coms.message(lambda message: message.text == 'Культорги')
async def command_KO(message: Message):
    id = message.from_user.id 
    if id not in data_about_users:
        data_about_users[id] = ['kult_kb', '', '', '', '']
    else:
        data_about_users[id][0] = 'kult_kb'
    await message.reply(
        text='Культорги КО-25',
        reply_markup = koms_layout.kult_kb 
    )

@user_router_coms.message(lambda message: message.text == 'Художники')
async def command_KO(message: Message):
    id = message.from_user.id 
    if id not in data_about_users:
        data_about_users[id] = ['art_kb', '', '', '', '']
    else:
        data_about_users[id][0] = 'art_kb'
    await message.reply(
        text = 'Художники КО-25',
        reply_markup = koms_layout.art_kb 
    )

@user_router_coms.message(lambda message: message.text == 'Поворята')
async def command_KO(message: Message):
    id = message.from_user.id 
    if id not in data_about_users:
        data_about_users[id] = ['cooker_kb', '', '', '', '']
    else:
        data_about_users[id][0] = 'cooker_kb'
    await message.reply(
        text = 'Поворята КО-25',
        reply_markup = koms_layout.cooker_kb
    )

@user_router_coms.message(lambda message: message.text == 'Макс Рябов')
async def command_KO(message: Message):
    photo_path = 'Files/Ryabov_M.jpg'  # Локальный путь к файлу с фото
    caption_text = (
        "*Рябов Максим*\n"
        "_Интересный факт:_\n"
        "Участвовал в голосующем КиВиНе 2018 года\n\n"
        "*Обо мне:*\n"
        "Я закончил 11-8 Физико-Математический класс в ФМШ. "
        "Сейчас являюсь автором этого телеграмм бота."
    )
    with open(photo_path, 'rb') as photo:
        await user_router_coms.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=caption_text,
            parse_mode='Markdown'
        )

