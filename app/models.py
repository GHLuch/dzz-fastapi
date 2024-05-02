import uuid
import datetime

from sqlalchemy import Column, String, select, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship


from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import mapped_column, Mapped, query
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    username: Mapped[str]
    email: Mapped[str]
    password_hash: Mapped[str]

    @classmethod
    async def create(cls, db: AsyncSession, **kwargs):
        transaction = cls(**kwargs)
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
    async def get_by_username(cls, db: AsyncSession, username: str):
        user = (await db.execute(select(cls).where(cls.username == username))).scalar()
        return user

    @classmethod
    async def get_all(cls, db: AsyncSession):
        return (await db.execute(select(cls))).scalars().all()

    processed_images: Mapped[list["ProcessedImages"]] = relationship(
        back_populates="user"
    )


class Models(Base):
    __tablename__ = "models"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str]

    @classmethod
    async def get_all(cls, db: AsyncSession):
        result = await db.execute(select(cls))
        return result.scalars().all()

    processed_images: Mapped[list["ProcessedImages"]] = relationship(
        back_populates="model"
    )


class ProcessedImages(Base):
    __tablename__ = "processed_images"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    model_id: Mapped[int] = mapped_column(ForeignKey("models.id"))
    hesh_img: Mapped[str]
    url_img: Mapped[str]
    create_time: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    @classmethod
    async def get_by_user_id(cls, db: AsyncSession, user_id: int):
        result = await db.execute(select(cls).where(cls.user_id == user_id))
        return result.scalar()

    user: Mapped[list["User"]] = relationship(back_populates="processed_images")
    model: Mapped[list["Models"]] = relationship(back_populates="processed_images")
