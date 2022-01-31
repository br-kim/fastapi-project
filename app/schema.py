from pydantic import BaseModel


class PostBase(BaseModel):
    email: str
    title: str
    content: str


class Post(PostBase):
    id: int

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass
