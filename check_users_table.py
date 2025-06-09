import asyncpg
import asyncio

DATABASE_URL = "postgresql://shezer_db_user:zk5eDxVZorkemREPa2oUDMyC7VEtzezR@dpg-d13cfb49c44c7395m4u0-a.oregon-postgres.render.com/shezer_db"

async def check_table_exists():
    conn = await asyncpg.connect(DATABASE_URL)
    query = """
    SELECT EXISTS (
        SELECT FROM information_schema.tables 
        WHERE table_name = 'users'
    );
    """
    result = await conn.fetchval(query)
    if result:
        print("✅ جدول 'users' موجود في قاعدة البيانات.")
    else:
        print("❌ جدول 'users' غير موجود.")
    await conn.close()

asyncio.run(check_table_exists())
