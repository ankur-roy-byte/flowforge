import asyncio

from app.db.init_db import init_db
from app.db.session import AsyncSessionLocal


async def main() -> None:
    async with AsyncSessionLocal() as session:
        await init_db(session)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(main())

