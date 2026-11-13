from app.database import AsyncSessionLocal
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    session = AsyncSessionLocal()

    try:
        yield session
    finally:
        await session.close()