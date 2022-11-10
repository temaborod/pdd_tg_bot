from aiogram.utils import executor
from create_bot import dp
from handlers import client, other


# команды в терминал о работе бота
async def on_startup(_):
    print('BOT IS ONLINE')


# хендлеры регистрируются по порядку: функция, в которой есть хендлер без аргумента - последняя
client.register_handlers_client(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  # skip_updates=True бот не ответит на сообщения,
                                                                      # пришедшие вне онлайн-сессии

                                                                      # on_startup=on_startup вызов функции при старте бота
                                                                      # с сообщением о том, что он онлайн в терминал