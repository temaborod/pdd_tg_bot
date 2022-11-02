import json
import os
from random import choice
from aiogram import types, Dispatcher
from create_bot import bot
#from inline_buttons.inline import inkb
from keyboard.client_kb import kb_client
from create_bot import dp


users = [681076159]

#@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    users = [681076159]
    if message.from_user.id in users:
        await bot.send_message(message.from_user.id, '<b>Привет!</b> Это бот для подготовки к экзамену ПДД', parse_mode="HTML",
                               reply_markup=kb_client)


@dp.message_handler(lambda message: message.from_user.id not in users, commands=['start', 'help', 'rules', 'test'])
async def some(message):
    print('unregistered user: ', message.from_user.id, ':::', message.from_user.first_name)
    await bot.send_message(message.from_user.id, 'Отказано в доступе!')


# @dp.message_handler(commands=['tests'])
async def start_test(message: types.Message):
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
        /help - помощь
        /rules - правила
        /test - начать тест
        ''')
    except:
        await message.answer('Try it now')




# @dp.message_handler(commands=['rules'])
async def rules_command(message: types.Message):
    await message.answer('''
    * Каждый вариант состоит из 40 вопросов
* Отвечаешь на вопрос - бот даст знать правильно ли ты ответил
* Ели ответ неверный - бот объяснит почему
* Как закончишь решать вариант - узнаешь свой результат
    ''')




# команды хендлеров для регистрации бота
def register_handlers_client(dp: Dispatcher, startwith=None):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(rules_command, commands=['rules'])
    dp.register_message_handler(start_test, commands=['test'])


