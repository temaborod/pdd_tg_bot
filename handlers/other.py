from aiogram import types, Dispatcher

# бот работает только с командами:
# @dp.message_handler()
async def empty(message: types.Message):
    await message.answer('There is no such command')
    await message.delete()

# функция регистрации хендлеров
def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(empty)
