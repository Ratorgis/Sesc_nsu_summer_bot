import os
import logging
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from Handlers.commands import user_router
#from Handlers.commands_privat import user_router_coms

load_dotenv(find_dotenv())
scheduler = AsyncIOScheduler(timezon = 'Asia/Novosibirsk')
admins = [int(admin) for admin in os.getenv('ADMINS')]

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

dp = Dispatcher(storage = MemoryStorage())
dp.include_router(user_router)
dp.include_router(user_router_coms)
bot = Bot(token = os.getenv('Token'), default = DefaultBotProperties(parse_mode = ParseMode.HTML))
