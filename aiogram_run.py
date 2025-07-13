import asyncio
from create_bot import dp, bot, scheduler
from Handlers.commands import user_router as start_router 
# from handlers.start import start_router 

async def main():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
