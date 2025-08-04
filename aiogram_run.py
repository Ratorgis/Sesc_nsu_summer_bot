import asyncio
from create_bot import dp, bot
from handlers.commands import user_router
from handlers.commands_privat import user_router_coms
from handlers.send_all_pics import phto_router

async def main():
    dp.include_router(user_router)
    dp.include_router(user_router_coms)
    dp.include_router(phto_router)
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
