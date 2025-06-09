# db.py
import asyncpg
import ssl

DB_URL = "postgres://your_user:your_password@your_host:your_port/your_db"

async def connect_db():
    try:
        ssl_context = ssl.create_default_context()
        conn = await asyncpg.connect(dsn=DB_URL, ssl=ssl_context)
        print("✅ تم الاتصال بقاعدة البيانات بنجاح")
        return conn
    except Exception as e:
        print(f"❌ فشل الاتصال بقاعدة البيانات:\n{e}")
        return None
