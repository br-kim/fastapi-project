from app.db.database import SessionMaker


async def get_db():
    session = SessionMaker()
    try:
        yield session
    finally:
        await session.commit()
        await session.close()
