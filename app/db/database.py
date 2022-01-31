from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, scoped_session

from app import config

SQLALCHEMY_DATABASE_URL = config.DATABASE_URL

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession))
Base = declarative_base()
