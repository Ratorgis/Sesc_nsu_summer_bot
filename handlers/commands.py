from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Router, F, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards import layout
from create_bot import admins, bot, news_channel_id, channel_id

def get_faq_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text = question, callback_data = f'faq_{i}')
        for i, question in enumerate(FAQ_text)
    ]
    return InlineKeyboardMarkup(inline_keyboard=[[btn] for btn in buttons])

class SaveState(StatesGroup):
    waiting_for_menu = State()
    waiting_for_news = State()

channel_router = Router()
user_router = Router()
users = []

saved_message = {
    'menu': None,
    'news': None
}

FAQ_ans = {
    'faq_0': 3,
    'faq_1': 5,
    'faq_2': 6,
    'faq_3': 7,
    'faq_4': 8,
    'faq_5': 10,
    'faq_6': 12
}

FAQ_text = [
    ('Что такое комсотряд ?'),
    ('Популярные места общежития'),
    ('Как постирать вещи ?'),
    ('Что-то сломалось в блоке. Что делать ?'),
    ('До куда можно выходить ученикам ЛШ-25'),
    ('Мне нужно за пределы академа'),
    ('Основное расписание на день')
]

#@user_router.message()
#async def print_msg_id(message: Message):
#    print(message.forward_from_message_id)


@user_router.message(CommandStart())
async def Start_message(message: Message):
    id = message.from_user.id 
    if id in admins:
        await message.answer(
            'Ты админ этого телеграмм-бота',
            reply_markup = layout.admin_main_kb
        )
    else:
        await bot.forward_message(
            chat_id = message.chat.id,
            message_id = 2,
            from_chat_id = news_channel_id
        )
        await message.answer(
            text = 'Для комуникации с ботом, используй кнопки на панели',
            reply_markup = layout.main_kb
        )
    if id not in users:
        users.append(id)
        print(users)


@user_router.callback_query(F.data.startswith('faq_'))
async def faq_callback(callback: types.CallbackQuery):
    await bot.forward_message(
        chat_id = callback.from_user.id,
        from_chat_id = news_channel_id,
        message_id =  FAQ_ans[callback.data]
    )
    await callback.answer()

@user_router.message(lambda message: message.text == 'Список Комс-Отряда')
async def list_coms_reply(message: Message):
    await message.answer(
        text = 'Выбери Комсенка',
        reply_markup = layout.group_choice_kb
    )

@user_router.message(lambda message: message.text == '< КО-25')
async def back_group_choice(message: Message):
    await message.answer(
        text = 'Хорошо',
        reply_markup = layout.group_choice_kb
    )

@user_router.message(lambda message: message.text == '< Главное Меню')
async def back_to_main(message: Message):
    id = message.from_user.id
    if id in admins:
        await message.answer(
            text = 'Вернулся к админской панели',
            reply_markup = layout.admin_main_kb
        )
    else:
        await message.answer(
            text = 'Ладно',
            reply_markup = layout.main_kb
        )

@user_router.message(lambda message: message.text == 'FAQ')
async def questions_message(message: Message):
    await message.answer(
        text = "Famoust Asking Question (Блок часто задаваемых вопросов), на которые мы постараемся ответить тут",
        reply_markup = get_faq_keyboard()
        )

@user_router.message(F.text == "Update_menu")
async def update_menu(message: Message, state: FSMContext):
    await message.answer("Перешли сообщение из канала, которое нужно сохранить")
    await state.set_state(SaveState.waiting_for_menu)

@user_router.message(F.text == "Update_news")
async def update_news(message: Message, state: FSMContext):
    await message.answer("Перешли сообщение из канала, которое нужно сохранить")
    await state.set_state(SaveState.waiting_for_news)

@user_router.message(SaveState.waiting_for_news)
async def save_channel_news(message: Message, state: FSMContext):
    if not message.forward_from_chat:
        return await message.answer("❌ Это не пересланное сообщение из канала.")
    saved_message["news"] = message.forward_from_message_id
    await state.clear()
    await message.answer("✅ Сообщение сохранено!")

@user_router.message(SaveState.waiting_for_menu)
async def save_channel_menu(message: Message, state: FSMContext):
    if not message.forward_from_chat:
        return await message.answer("❌ Это не пересланное сообщение из канала.")
    saved_message["menu"] = message.forward_from_message_id
    await state.clear()
    await message.answer("✅ Сообщение сохранено!")

@user_router.message(F.text == "Меню")
async def send_saved_menu(message: Message):
    await bot.forward_message(
        chat_id = message.chat.id,
        from_chat_id = news_channel_id,
        message_id = saved_message['menu']
    )

@user_router.message(F.text == "Мероприятия")
async def send_saved_news(message: Message):
    await bot.forward_message(
        chat_id = message.chat.id,
        from_chat_id = news_channel_id,
        message_id = saved_message['news']
    )


