from collections.abc import AsyncGenerator

from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from core.settings import settings

engine = create_async_engine(settings.db_url, echo=False, pool_size=20, max_overflow=5)

session_maker = async_sessionmaker(engine, expire_on_commit=False, autocommit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_maker() as session:
        yield session


async def get_redis():
    redis = await Redis.from_url(settings.redis_url, decode_responses=True)
    async with redis as r:
        yield r
