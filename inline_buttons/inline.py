from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# кнопка- ссылка
urlkb = InlineKeyboardMarkup(row_width=1)  # по 1 кнопке в ряд
# создание инлайн кнопок
urlButton1 = InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/watch?v=gpCIfQUbYlY&list=PLNi5HdK6QEmX1OpHj0wvf8Z28NYoV5sBJ&index=9')
urlButton2 = InlineKeyboardButton(text='Translator', url='https://translate.yandex.ru/?lang=ru-en')

urlkb.add(urlButton1, urlButton2)  # добавляем кнопки

