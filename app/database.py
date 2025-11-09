from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from collections.abc import AsyncGenerator


from app.config import settings


DATABASE_URL_asyncpg = settings.DATABASE_URL_asyncpg
async_engine  = create_async_engine(DATABASE_URL_asyncpg)
async_session_factory  = async_sessionmaker(autocommit=False, autoflush=False, bind=async_engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_session() -> AsyncGenerator:
    async with async_session_factory() as session:
        yield session