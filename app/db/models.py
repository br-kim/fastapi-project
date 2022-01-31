from sqlalchemy import Column, Integer, String, Text

from app.db.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    title = Column(String)
    content = Column(Text)
