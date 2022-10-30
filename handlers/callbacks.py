import os
import json

from aiogram import types
from create_bot import bot, dp

@dp.callback_query_handler(lambda callback_query: True)
async def callback_handler(callback_query: types.CallbackQuery):
    try:

        data = callback_query.data
        temp = data.split("_")

        if len(temp) == 3:

            ticket, question, correct = temp[0], int(temp[1]), int(temp[2])

            file = open(os.getcwd() + "/tickets/" + ticket, encoding="UTF-8")
            data = json.loads(file.read())
            file.close()

            buttons = []
            count = 0
            for jojo in data[question]["answers"]:
                buttons.append(types.InlineKeyboardButton(text=jojo["name"], callback_data=ticket + "_" + str(question) + "_" + str(count) + "_" + str(correct)))
                count += 1

            keyboard = types.InlineKeyboardMarkup(row_width=1)
            keyboard.add(*buttons)

            await bot.delete_message(message_id=callback_query.message.message_id, chat_id=callback_query.from_user.id)
            return await bot.send_video(video=data[question]["video"], chat_id=callback_query.from_user.id, caption=data[question]["question"], reply_markup=keyboard)

        if len(temp) == 4:

            ticket, question, answer, correct = temp[0], int(temp[1]), int(temp[2]), int(temp[3])

            file = open(os.getcwd() + "/tickets/" + ticket, encoding="UTF-8")
            data = json.loads(file.read())
            file.close()

            message = data[question]["question"] + "\n\nВаш ответ: " + data[question]["answers"][answer]['name'] + "\n"
            message += ("Ответ верный!", "Ответ неверный!\n\nПравильный ответ: " + data[question]["correct"])[(data[question]["correct"] == data[question]["answers"][answer]['name']) is False]
            message += ("", "\n\nОбъяснение:\n" + data[question]["exp"])[(data[question]["correct"] == data[question]["answers"][answer]['name']) is False]

            if data[question]["correct"] == data[question]["answers"][answer]['name']:
                correct+=1

            buttons = [types.InlineKeyboardButton(text="Следующий вопрос", callback_data=ticket + "_" + str(question + 1) + "_" + str(correct))]
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            keyboard.add(*buttons)

            if len(data) == question + 1:

                keyboard = None
                message = "Тест завершён!\nРезультат: " + str(correct) +"/40\n\n" + message

            return await bot.edit_message_caption(message_id=callback_query.message.message_id, chat_id=callback_query.from_user.id, caption=message, reply_markup=keyboard)

    except Exception as e:
        print(repr(e))