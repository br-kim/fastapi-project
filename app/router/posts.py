from fastapi import APIRouter, Depends, Response

from app.deps import get_db
from app.db.crud import get_post_db, write_post_db

from app.schema import PostCreate, Post

posts_router = APIRouter()


@posts_router.get("/{post_num}", response_model=Post)
async def get_post(post_num: int, db=Depends(get_db)):
    db_post = await get_post_db(db, post_num)
    if not db_post:
        return Response(status_code=404)
    return Post.from_orm(db_post)


@posts_router.post("")
async def write_post(post: PostCreate, db=Depends(get_db)):
    return await write_post_db(db, post)
