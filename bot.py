import logging

import requests

import config

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = config.SECRET_KEY

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.get_args()
    chat_id = message.chat.id
    response = requests.post(
        url=f"http://127.0.0.1:8000/profile/get-chat-id?user_id={user_id}&chat_id={chat_id}"
    )
    await message.reply(f"🥳 Твой телеграм был успешно привязан к учетной записи!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
