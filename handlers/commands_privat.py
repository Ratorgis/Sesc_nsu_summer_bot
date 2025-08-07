from aiogram.types import Message
from aiogram import Router
from keyboards import koms_layout
from create_bot import news_channel_id

user_router_coms = Router()

reply_kbds = {
    'Физорги': [koms_layout.phys_kb, 'Ежедневно проводят зарядку, спортивные активности и матчи'],
    'Культорги': [koms_layout.kult_kb, 'Готовят самые яркие мероприятия'],
    'Художники': [koms_layout.art_kb, 'Занимаюстя оформлением и дизайном всей Летней школы'],
    'Поварята': [koms_layout.cooker_kb, 'Помогают в столовой и вкусно кормят вас']
}

@user_router_coms.message(lambda message: message.text in reply_kbds.keys())
async def test_func(message: Message):
    await message.answer(
        text = reply_kbds[message.text][1],
        reply_markup = reply_kbds[message.text][0]
    )
