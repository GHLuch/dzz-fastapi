import uuid

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import mapped_column, Mapped, query
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    email: Mapped[str]
    password_hash: Mapped[str]

    @classmethod
    async def create(cls, db: AsyncSession, **kwargs):
        transaction = cls(id=id, **kwargs)
        db.add(transaction)
        await db.commit()
        await db.refresh(transaction)
        return transaction

    @classmethod
    async def get(cls, db: AsyncSession, id: str):
        try:
            transaction = await db.get(cls, id)
        except NoResultFound:
            return None
        return transaction

    @classmethod
    async def get_by_email(cls, db: AsyncSession, email: str):
        user = (await db.execute(select(cls).where(cls.email == email))).scalar()
        return user

    @classmethod
    async def get_all(cls, db: AsyncSession):
        return (await db.execute(select(cls))).scalars().all()
