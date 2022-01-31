from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert

from app.db.models import Post


async def get_post_db(session: AsyncSession, post_num):
    stmt = select(Post).where(Post.id == post_num)
    post = await session.execute(stmt)
    return post.scalar()


async def write_post_db(session: AsyncSession, post):
    stmt = insert(Post).values(post.dict())
    result = await session.execute(stmt)
    return result.inserted_primary_key
