from aiogram import types, Dispatcher
import json
import string
from create_bot import dp

# @dp.message_handler()
async def no_swearing(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('censorship.json')))) != set():
        await message.reply('Маты запрещены!')
        await message.delete()

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(no_swearing)
