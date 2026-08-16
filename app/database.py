import os
import asyncio
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, connect_args={"connect_timeout": 10})

async def test_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("Database connection successful")
    except Exception as e:
        print(f" Database connection failed: {e}")



async def main():
    await test_connection()

if __name__ == "__main__":
    asyncio.run(main())