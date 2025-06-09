# init_db.py
import asyncio
import ssl
import asyncpg

DB_URL = "postgresql://shezer_db_user:zk5eDxVZorkemREPa2oUDMyC7VEtzezR@dpg-d13cfb49c44c7395m4u0-a.oregon-postgres.render.com/shezer_db"

async def create_tables():
    ssl_context = ssl.create_default_context()
    conn = await asyncpg.connect(dsn=DB_URL, ssl=ssl_context)

    await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            telegram_id BIGINT UNIQUE NOT NULL,
            username TEXT,
            country TEXT,
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    await conn.close()
    print("✅ تم إنشاء جدول المستخدمين بنجاح")

if __name__ == "__main__":
    asyncio.run(create_tables())
