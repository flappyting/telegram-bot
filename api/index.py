import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message()
async def handle_start(message: types.Message):
    if message.text == "/start":
        await message.answer(
            "您好 👋 欢迎使用 Service Bridge Bot!\n\n"
            "我目前提供 +888 匿名 Telegram 号码出租，近期将新增 200-400 个号码。\n\n"
            "📌 当前促销价格（库存有限）:\n"
            "30 天 – 45 USD\n"
            "60 天 – 81 USD\n"
            "90 天 – 115 USD\n\n"
            "✅ 所有流程自动完成 👉 @rentitnumbersbot\n"
            "❓ 如有疑问请联系我 👉 @rentit"
        )

async def handle(request):
    body = await request.json()
    update = types.Update(**body)
    await dp.feed_update(bot, update)
    return web.Response()

app = web.Application()
app.router.add_post("/", handle)
