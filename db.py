# db.py
import asyncpg
import ssl

DB_URL = "postgresql://postgres:shezer2025$@db.kkblzjitvdcydonfssed.supabase.co:5432/postgres"

async def connect_db():
    try:
        ssl_context = ssl.create_default_context()
        conn = await asyncpg.connect(dsn=DB_URL, ssl=ssl_context)
        print("✅ تم الاتصال بقاعدة البيانات بنجاح")
        return conn
    except Exception as e:
        print(f"❌ فشل الاتصال بقاعدة البيانات:\n{e}")
        return None
