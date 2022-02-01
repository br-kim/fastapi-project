import asyncio

import pytest_asyncio
from httpx import AsyncClient

from app import main
from app.main import engine, Base
from app.deps import get_db
from app.db.crud import write_post_db
from app.schema import PostCreate


async def set_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    post = PostCreate(email="test@test.com", title="테스트 글", content="테스트 내용")
    async for session in get_db():
        await write_post_db(session, post)


@pytest_asyncio.fixture(scope="session")
async def client():
    async with AsyncClient(app=main.app, base_url="http://127.0.0.1") as client:
        await set_db()
        yield client


@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

