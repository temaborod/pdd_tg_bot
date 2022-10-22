from aiogram import types, Dispatcher
from create_bot import dp, bot


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'HIII')
        await message.delete()
    except:
        await message.answer('Try it now')


# @dp.message_handler(commands=['rules'])
async def rules_command(message: types.Message):
    await message.answer('Каждый вариант состоит из 40 вопросов')
    #await bot.send_message(message.from_user.id, 'Каждый вариант состоит из 40 вопросов')

# команды хендлеров для регистрации бота
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(rules_command, commands=['rules'])