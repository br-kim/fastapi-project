from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import engine


async def get_db() -> AsyncSession:
    session = AsyncSession(bind=engine)
    try:
        yield session
    finally:
        await session.commit()
        await session.close()
