# bot.py
import asyncio
from db import connect_db

async def main():
    conn = await connect_db()
    if not conn:
        print("❌ لا يمكن المتابعة بدون اتصال بقاعدة البيانات")
        return

    print("✅ البوت شغال الآن...")

if __name__ == "__main__":
    asyncio.run(main())
