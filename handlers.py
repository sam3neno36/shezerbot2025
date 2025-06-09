from aiogram import types

async def handle_start(message: types.Message, conn):
    user = message.from_user
    await conn.execute(
        "INSERT INTO users (telegram_id, username, country) VALUES ($1, $2, $3) ON CONFLICT (telegram_id) DO NOTHING",
        user.id, user.username, user.language_code
    )
    await message.answer(f"مرحباً بك {user.first_name}! 👋\nاستخدم الأزرار لتصفح المنتجات.")

async def handle_callback(callback_query: types.CallbackQuery, conn):
    await callback_query.answer("تم الضغط على زر (سيتم تطوير المحتوى لاحقاً).")