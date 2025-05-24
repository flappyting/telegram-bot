# /api/index.py

import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# Initialisierung
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Message-Handler
@dp.message()
async def handle_start(message: types.Message):
    if message.text == "/start":
        await message.answer("Test erfolgreich. ✅")

# Webhook-Handler
async def handle(request):
    body = await request.json()
    update = types.Update(**body)
    await dp.feed_update(bot, update)
    return web.Response(text="ok")

# Aiohttp-Anwendung vorbereiten
app = web.Application()
app.router.add_post("/", handle)

# 🟢 Vercel erwartet diesen Handler genau so:
# KEINE Funktion definieren! Gib Vercel direkt das App-Objekt:
handler = app

