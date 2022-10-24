from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# создание кнопок
b1 = KeyboardButton('/start')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/rules')
b4 = KeyboardButton('/test')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)  # создание клавиатуры

kb_client.row(b1, b2, b3).add(b4)  # добавление кнопок


