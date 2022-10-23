from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboard import kb_client

# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Hi! I'm a bot!", reply_markup=kb_client)

    except:
        await message.answer('Try it now')

# @dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,\
        '''
        Commands:
        /start - старт бота
        /help - помощь
        /rules - правила
        ''')

    except:
        await message.answer('Try it now')

# @dp.message_handler(commands=['rules'])
async def rules_command(message: types.Message):
    await message.answer('Каждый вариант состоит из 40 вопросов''')
    #await bot.send_message(message.from_user.id, 'Каждый вариант состоит из 40 вопросов')


# команды хендлеров для регистрации бота
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(rules_command, commands=['rules'])
