from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

bot = Bot(token=os.getenv('TOKEN'))  # инициализация бота, чтение токена
dp = Dispatcher(bot)  # инициализация Dispatcher

