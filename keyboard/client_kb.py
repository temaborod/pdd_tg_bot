from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/rules')
# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton('Отправить где я', request_location=True)  # тг на компе не может отправить расположение, телефон может
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

# kb_client.add(b1).insert(b2).add(b3)  # добавляет кнопки в клаву с новой строки \\ insert - добавит рядом с предыдущей кнопкой
kb_client.row(b1, b2, b3).#row(b4, b5)  # добавить все кнопки в строку