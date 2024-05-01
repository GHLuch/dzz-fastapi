import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.database import get_db
from app.utils import get_hashed_password

from ..models import User as UserModel

user_router = APIRouter(prefix="/user", tags=["user"])


class UserSchemaBase(BaseModel):
    username: str
    email: str 
    password: str


class UserSchemaCreate(UserSchemaBase):
    pass


class UserSchema(BaseModel):
    id: uuid.UUID
    username: str
    email: str
    

    class Config:
        orm_mode = True


@user_router.get("/get-user", response_model=UserSchema)
async def get_user(id: str, db: AsyncSession = Depends(get_db)):
    user = await UserModel.get(db, id)
    return user


@user_router.get("/get-users", response_model=list[UserSchema])
async def get_users(db: AsyncSession = Depends(get_db)):
    users = await UserModel.get_all(db)
    return users


@user_router.post("/create-user", response_model=UserSchema)
async def create_user(user: UserSchemaCreate, db: AsyncSession = Depends(get_db)):
    user_db = await UserModel.get_by_email(db, user.email)
    if user_db is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists for this email")

    user_db = await UserModel.get_by_username(db, user.username)
    if user_db is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists for this username")
    user_for_db = {
        "username": user.username,
        "email": user.email,
        "password_hash": get_hashed_password(user.password)
    }
    user = await UserModel.create(db, **user_for_db)
    return user
