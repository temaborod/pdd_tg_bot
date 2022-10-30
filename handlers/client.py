import json
import os
from random import choice

from aiogram import types, Dispatcher

from create_bot import bot
from inline_buttons.inline import inkb


#answ = dict()

# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:

        if message.from_user.id != message.chat.id:
            return

        tickets = os.listdir(os.getcwd() + "/tickets")
        ticket = choice(tickets)

        file = open(os.getcwd() + "/tickets/" + ticket, encoding="UTF-8")
        data = json.loads(file.read())
        file.close()

        buttons = []
        count = 0
        for jojo in data[0]["answers"]:
            buttons.append(types.InlineKeyboardButton(text=jojo["name"], callback_data=ticket + "_0_" + str(count) + "_0"))
            count += 1

        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)

        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await bot.send_video(chat_id=message.from_user.id, video=data[0]["video"], caption=data[0]["question"], reply_markup=keyboard)
    except Exception as e:
        print(repr(e))
        await message.answer('Try it now')


# @dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, '''
        Commands:
        /start - старт бота
        /help - помощь
        /rules - правила
        /test - начать тест
        ''')
    except:
        await message.answer('Try it now')


# @dp.message_handler(commands=['rules'])
async def rules_command(message: types.Message):
    await message.answer('''
    Каждый вариант состоит из 40 вопросов
Отвечаешь на вопрос - бот даст знать правильно ли ты ответил
Ели ответ неверный - бот объяснит почему
Как закончишь решать вариант - узнаешь свой результат
    ''')


# команда начала теста по кнопке из client_kb
# @dp.message_handler(commands=['test'])
async def start_test(message: types.Message):
    await message.answer('Inline callback button', reply_markup=inkb)


# хендлер для callback button
#@dp.message_handler(commands=['test_callback'])
# async def test_callback_button(message: types.Message):
#     await message.answer('Inline callback button', reply_markup=inkb)


# хендлер для callback (что он вернет)
# @dp.callback_query_handler(Text(startswith='like_'))
# async def www_call(callback: types.CallbackQuery):
#     result = int(callback.data.split('_')[1])
#     #await callback.answer('Вы проголосовали')
#
#     # чтобы пользоватеь не проголосовал 2 раза
#     if f'{callback.from_user.id}' not in answ:
#         answ[f'{callback.from_user.id}'] = result
#         await callback.answer('Вы проголосовали')
#     else:
#         await callback.answer('Вы уже проголосовали', show_alert=True)


# команды хендлеров для регистрации бота
def register_handlers_client(dp: Dispatcher, startwith=None):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(rules_command, commands=['rules'])
    dp.register_message_handler(start_test, commands=['test'])


