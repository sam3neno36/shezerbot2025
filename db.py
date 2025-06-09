# db.py
import asyncpg
import ssl

DB_URL = "postgresql://shezer_db_user:zk5eDxVZorkemREPa2oUDMyC7VEtzezR@dpg-d13cfb49c44c7395m4u0-a.oregon-postgres.render.com/shezer_db"

async def connect_db():
    try:
        ssl_context = ssl.create_default_context()
        conn = await asyncpg.connect(dsn=DB_URL, ssl=ssl_context)
        print("✅ تم الاتصال بقاعدة البيانات بنجاح")
        return conn
    except Exception as e:
        print(f"❌ فشل الاتصال بقاعدة البيانات:\n{e}")
        return None
