import logging
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
    await message.reply(f"User_id: {user_id}\nChat_id: {chat_id}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)