# test_db.py
import asyncio
import asyncpg

DB_URL = "postgresql://postgres:Shezer2025Shezer20251010@db.kkblzjitvdcydonfssed.supabase.co:5432/postgres"

async def main():
    try:
        conn = await asyncpg.connect(dsn=DB_URL, timeout=10)
        print("✅ تم الاتصال بقاعدة البيانات بنجاح")
        await conn.close()
    except Exception as e:
        print("❌ فشل الاتصال بقاعدة البيانات:")
        print(e)

if __name__ == "__main__":
    asyncio.run(main())
