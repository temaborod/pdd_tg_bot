from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()


bot = Bot(token=os.getenv('TOKEN'))  # инициализация бота, чтение токена
dp = Dispatcher(bot, storage=storage)  # инициализация Dispatcher


