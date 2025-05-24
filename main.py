import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import setup_application
from aiohttp import web
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message()
async def handle_start(message: types.Message):
    if message.text == "/start":
        await message.answer(
            "您好 👋 欢迎使用 Service Bridge Bot!\n\n"
            "我目前提供 +888 匿名 Telegram 号码出租，近期将新增 200-400 个号码。\n\n"
            "📦 当前促销价格 (库存有限)：\n"
            "30 天 – 45 USD\n"
            "60 天 – 81 USD\n"
            "90 天 – 115 USD\n\n"
            "✅ 所有流程自动完成 👉 @rentitnumbersbot\n"
            "📩 如有疑问请联系我 👉 @rentit"
        )

async def on_startup(app: web.Application):
    webhook_url = os.getenv("WEBHOOK_URL")
    await bot.set_webhook(webhook_url)

async def on_shutdown(app: web.Application):
    await bot.delete_webhook()
    await bot.session.close()

def create_app():
    app = web.Application()
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    setup_application(app, dp)
    return app

app = create_app()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    web.run_app(app, port=int(os.getenv("PORT", 8000)))
