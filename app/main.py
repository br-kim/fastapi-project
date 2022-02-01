import uvicorn
from fastapi import FastAPI

from app.router.index import index_router
from app.router.posts import posts_router
from app.db.models import Base
from app.db.database import engine
from app.config import DOCS_URL, REDOC_URL


app = FastAPI(docs_url=DOCS_URL, redoc_url=REDOC_URL)
app.include_router(index_router)
app.include_router(posts_router, prefix="/posts")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
