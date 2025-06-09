# bot.py
import asyncio
import ssl
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from db import connect_db

# 🔐 ضع التوكن الخاص بك هنا
BOT_TOKEN = "8044205270:AAHkxRdbJ9GvggNb_Uq3w9eVjAukRW8xOxw"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or ""
    country = message.from_user.language_code or "unknown"

    conn = await connect_db()
    if conn is None:
        await message.answer("⚠️ حدث خطأ في الاتصال بقاعدة البيانات.")
        return

    try:
        user_exists = await conn.fetchval("SELECT 1 FROM users WHERE telegram_id = $1", user_id)
        if user_exists:
            await message.answer("👋 مرحبًا بعودتك!")
        else:
            await conn.execute(
                "INSERT INTO users (telegram_id, username, country) VALUES ($1, $2, $3)",
                user_id, username, country
            )
            await message.answer("🎉 تم تسجيلك بنجاح!")
    except Exception as e:
        await message.answer(f"❌ حدث خطأ أثناء حفظ بياناتك: {e}")
    finally:
        await conn.close()

# ✅ تشغيل البوت
async def main():
    conn = await connect_db()
    if conn is None:
        print("❌ لا يمكن المتابعة بدون اتصال بقاعدة البيانات")
        return
    await conn.close()
    print("✅ البوت شغال الآن...")
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
