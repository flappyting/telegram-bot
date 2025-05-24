from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import asyncio
from keep_alive import keep_alive

API_TOKEN = "7508564868:AAH5Lk4VgIrYMN5wwbajqe1loWKXQXPcULw"

bot = Bot(token=API_TOKEN,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message()
async def handle_start(message: types.Message):
    if message.text == "/start":
        await message.answer(
            "您好 👋 欢迎使用 Service Bridge Bot！\n\n"
            "我目前提供 +888 匿名 Telegram 号码出租，近期将新增 200–400 个号码。\n\n"
            "📦 当前促销价格（库存有限）:\n"
            "30 天 - 45 USD\n"
            "60 天 - 81 USD\n"
            "90 天 - 115 USD\n\n"
            "✅ 所有流程自动完成 👉 @rentitnumbersbot\n"
            "📩 如有疑问请联系我 👉 @rentit"
        )


async def main():
    keep_alive()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
