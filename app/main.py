import uvicorn
from fastapi import FastAPI

from app.router.index import index_router

app = FastAPI()
app.include_router(index_router)


if __name__ == "__main__":
    uvicorn.run("main:app")
