import json
import os
import uuid
from random import choice
from aiogram import types, Dispatcher
from create_bot import bot
from keyboard.client_kb import kb_client
from create_bot import dp



#@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):

    if not os.path.isfile(os.getcwd() + "/codes.json"):
        file = open(os.getcwd() + "/codes.json", "+w");
        file.close()

    data = []

    file = open(os.getcwd() + "/codes.json", "r", encoding="UTF-8")
    data = json.load(file)
    file.close()

    item = []
    boolean = False
    for temp in data:
        if temp["id"] == message.from_user.id:
            boolean = True

    if boolean == True:
        await message.answer("всё гуд", reply_markup=kb_client)
    else:
        await message.answer("всё не гуд,\nВведите : /code <код>")


@dp.message_handler(lambda message: check(message.from_user.id) == False, commands=['help', 'rules', 'test'])
async def some(message):
    print('unregistered user: ', message.from_user.id, ':::', message.from_user.first_name)
    with open("unregistered user.txt", "a") as f:
        f.write('unregistered user: ' + str(message.from_user.id) + ' ::: ' + message.from_user.first_name + "\n")
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

async def generate_code(message: types.Message):
    try:
        if message.from_user.id != 681076159:
            return

        value = int(message.text.replace("/generate ", ""))

        if not os.path.isfile(os.getcwd() + "/codes.json"):
            file = open(os.getcwd() + "/codes.json", "+w");
            file.close()

        data = []

        file = open(os.getcwd() + "/codes.json", "r", encoding="UTF-8")
        data = json.load(file)
        file.close()

        for _ in range(value):
            code = str(uuid.uuid4())
            entity = {"code": code, "id": None}
            data.append(entity)
            await message.answer(code)

        file = open(os.getcwd() + "/codes.json", "+w")
        json.dump(data, file, ensure_ascii=False, indent=4)
        file.close()

    except Exception as e:
        print(e)
        await message.answer('Try it now')

async def confirm_code(message: types.Message):
    try:
        if check(message.from_user.id):
            return await message.answer("идика ты нахуй")

        value = message.text.replace("/code ", "")

        if not os.path.isfile(os.getcwd() + "/codes.json"):
            return

        data = []

        file = open(os.getcwd() + "/codes.json", "r", encoding="UTF-8")
        data = json.load(file)
        file.close()

        item = []
        boolean = False
        for temp in data:
            if temp["code"] == value:
                if temp["id"] is None:
                    temp["id"] = message.from_user.id
                    boolean = True
                    await message.answer("Welcome", reply_markup=kb_client)

            item.append(temp)

        if boolean == False:
            await message.answer("Код не найден..")
        else:
            file = open(os.getcwd() + "/codes.json", "+w")
            json.dump(data, file, ensure_ascii=False, indent=4)
            file.close()

    except Exception as e:
        print(e)
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


def check(value):
    if not os.path.isfile(os.getcwd() + "/codes.json"):
        file = open(os.getcwd() + "/codes.json", "+w");
        file.close()

    data = []

    file = open(os.getcwd() + "/codes.json", "r", encoding="UTF-8")
    data = json.load(file)
    file.close()

    item = []
    boolean = False
    for temp in data:
        if temp["id"] == value:
            boolean = True

    return boolean

# команды хендлеров для регистрации бота
def register_handlers_client(dp: Dispatcher, startwith=None):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(rules_command, commands=['rules'])
    dp.register_message_handler(start_test, commands=['test'])
    dp.register_message_handler(generate_code, commands=['generate'])
    dp.register_message_handler(confirm_code, commands=['code'])


