import asyncpg
import asyncio

DATABASE_URL = "postgresql://shezer_db_user:zk5eDxVZorkemREPa2oUDMyC7VEtzezR@dpg-d13cfb49c44c7395m4u0-a.oregon-postgres.render.com/shezer_db"

async def create_users_table():
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            telegram_id BIGINT UNIQUE NOT NULL,
            username TEXT,
            country TEXT,
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    print("✅ تم إنشاء جدول 'users' (أو هو موجود مسبقًا).")
    await conn.close()

asyncio.run(create_users_table())
