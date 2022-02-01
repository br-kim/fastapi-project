from asyncio import current_task

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session
from sqlalchemy.orm import sessionmaker

from app import config


engine = create_async_engine(config.DATABASE_URL)
async_session_factory = sessionmaker(autocommit=False, autoflush=True, bind=engine, class_=AsyncSession)
SessionMaker = async_scoped_session(async_session_factory, scopefunc=current_task)
Base = declarative_base()
