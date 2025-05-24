# /api/index.py

import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message()
async def handle_start(message: types.Message):
    if message.text == "/start":
        await message.answer("Test erfolgreich.")

async def handle(request):
    body = await request.json()
    update = types.Update(**body)
    await dp.feed_update(bot, update)
    return web.Response(text="ok")

app = web.Application()
app.router.add_post("/", handle)

# Wichtig: Vercel sucht nach einer async-Methode namens `app`
async def handler(request):
    return await app._handle(request)

# export
# (damit Vercel weiß, welche Funktion zu verwenden ist)
__all__ = ["handler"]

