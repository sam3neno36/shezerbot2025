import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = "8044205270:AAHkxRdbJ9GvggNb_Uq3w9eVjAukRW8xOxw"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# نفس handler البداية
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("👋 مرحبًا! البوت يعمل بنظام polling و الويب سيرفر مفتوح")

async def on_startup(dispatcher):
    print("🔵 بوت بدأ العمل!")

async def web_handler(request):
    return web.Response(text="بوتك يعمل والويب سيرفر شغال 👍")

async def main():
    # تهيئة ويب سيرفر aiohttp
    app = web.Application()
    app.add_routes([web.get('/', web_handler)])

    # احصل على PORT من متغيرات البيئة أو 8000 كافتراضي
    port = int(os.getenv('PORT', 8000))

    # شغل ويب سيرفر aiohttp بشكل غير متزامن
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"🌐 الويب سيرفر يعمل على المنفذ {port}")

    # شغل البوت polling (يحجز الـ event loop الرئيسي)
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
