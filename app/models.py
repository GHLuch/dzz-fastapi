from uuid import uuid4
import datetime

from sqlalchemy import Column, String, select, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)

    @classmethod
    async def create(cls, db: AsyncSession, id=None, **kwargs):
        if not id:
            id = uuid4().hex

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
    async def get_all(cls, db: AsyncSession):
        return (await db.execute(select(cls))).scalars().all()
    
    processed_images: Mapped[list["ProcessedImages"]] = relationship (
        back_populates="user"
    )
    
    

 
class Models(Base):
    __tablename__ = "models"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    processed_images: Mapped[list["ProcessedImages"]] = relationship (
        back_populates="model"
    )


class ProcessedImages(Base):
    __tablename__ = "processed_images"
    id: Mapped[int] =  mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    model_id: Mapped[int] = mapped_column(ForeignKey("models.id"))
    hesh_img: Mapped[str]
    url_img: Mapped[str]
    create_time: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


    user: Mapped[list["User"]] = relationship (
        back_populates="processed_images"
    )
    model: Mapped[list["Models"]] = relationship (
        back_populates="processed_images"
    )

   
