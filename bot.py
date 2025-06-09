import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.dispatcher.router import Router
import asyncpg

# إعدادات
BOT_TOKEN = "8044205270:AAHkxRdbJ9GvggNb_Uq3w9eVjAukRW8xOxw"
DATABASE_URL = "postgresql://shezer_db_user:zk5eDxVZorkemREPa2oUDMyC7VEtzezR@dpg-d13cfb49c44c7395m4u0-a.oregon-postgres.render.com/shezer_db"

bot = Bot(token=BOT_TOKEN)
router = Router()
dp = Dispatcher()
dp.include_router(router)


# 🧠 تسجيل المستخدم
async def register_user(user_id: int, username: str):
    conn = await asyncpg.connect(DATABASE_URL)
    user = await conn.fetchrow("SELECT * FROM users WHERE telegram_id = $1", user_id)
    if not user:
        await conn.execute(
            "INSERT INTO users (telegram_id, username) VALUES ($1, $2)",
            user_id, username
        )
        print(f"🟢 تم تسجيل مستخدم جديد: {username} ({user_id})")



@router.message()
async def echo_all(message: Message):
    await message.answer("✅ تم استلام رسالتك.")
