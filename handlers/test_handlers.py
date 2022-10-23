# from other
# фильтр матов
# @dp.message_handler()
# async def no_swearing(message: types.Message):
#     if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
#             .intersection(set(json.load(open('censorship.json')))) != set():
#         await message.reply('Маты запрещены!')
#         await message.delete()


# b5 = KeyboardButton('Поделиться номером', request_contact=True)
# b6 = KeyboardButton('Отправить где я', request_location=True)  # тг на компе не может отправить расположение, телефон может