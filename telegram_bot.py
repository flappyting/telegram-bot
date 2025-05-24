import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

API_TOKEN = "7508564868:AAH5Lk4VgIrYMN5wwbajqe1loWKXQXPcULw"

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

@dp.message()
async def handle_message(message: Message):
    if message.text == "/start":
        await message.answer("您好 👋 欢迎使用 Service Bridge Bot<br>请点击 👉 <a href='https://t.me/rentit'>@rentit</a> 了解更多")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())