from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.database import get_db
from app.utils import get_hashed_password

from ..models import User as UserModel

router = APIRouter(prefix="/user", tags=["user"])


class UserSchemaBase(BaseModel):
    email: str 
    password: str


class UserSchemaCreate(UserSchemaBase):
    pass


class UserSchema(UserSchemaBase):
    id: str

    class Config:
        orm_mode = True


@router.get("/get-user", response_model=UserSchema)
async def get_user(id: str, db: AsyncSession = Depends(get_db)):
    user = await UserModel.get(db, id)
    return user


@router.get("/get-users", response_model=list[UserSchema])
async def get_users(db: AsyncSession = Depends(get_db)):
    users = await UserModel.get_all(db)
    return users


@router.post("/create-user", response_model=UserSchema)
async def create_user(user: UserSchemaCreate, db: AsyncSession = Depends(get_db)):
    user_db = await UserModel.get_by_email(db, user.email)
    if user_db is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists for this email")
    user_for_db = {
        "email": user.email,
        "password_hash": get_hashed_password(user.password)
    }
    user = await UserModel.create(db, **user_for_db)
    return user
