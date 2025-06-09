import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
import asyncpg

BOT_TOKEN = "8044205270:AAHkxRdbJ9GvggNb_Uq3w9eVjAukRW8xOxw"
DATABASE_URL = "postgresql://shezer_db_user:zk5eDxVZorkemREPa2oUDMyC7VEtzezR@dpg-d13cfb49c44c7395m4u0-a.oregon-postgres.render.com/shezer_db"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


# تسجيل المستخدم في قاعدة البيانات
async def register_user(user_id: int, username: str):
    conn = await asyncpg.connect(DATABASE_URL)
    user = await conn.fetchrow("SELECT * FROM users WHERE telegram_id = $1", user_id)
    if not user:
        await conn.execute(
            "INSERT INTO users (telegram_id, username) VALUES ($1, $2)",
            user_id, username
        )
        print(f"🟢 تم تسجيل مستخدم جديد: {username} ({user_id})")
    else:
        print(f"🔁 المستخدم موجود مسبقًا: {username} ({user_id})")
    await conn.close()


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await register_user(message.from_user.id, message.from_user.username or "no_username")
    await message.answer("👋 أهلًا بك! تم تسجيلك بنجاح.")


# ويب سيرفر aiohttp
async def web_handler(request):
    return web.Response(text="بوتك يعمل والويب سيرفر شغال 👍")


async def main():
    # aiohttp web server
    app = web.Application()
    app.add_routes([web.get('/', web_handler)])
    port = int(os.getenv('PORT', 8000))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"🌐 الويب سيرفر يعمل على المنفذ {port}")

    # bot polling
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
