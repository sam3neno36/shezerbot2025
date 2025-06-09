import asyncpg
import os

# ⚠️ تأكد من تعديل بيانات الاتصال بقاعدة البيانات هنا
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Shezer2025Shezer20251010@db.kkblzjitvdcydonfssed.supabase.co:5432/postgres")

async def connect_db():
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print(f"❌ خطأ في الاتصال بقاعدة البيانات: {e}")
        return None
