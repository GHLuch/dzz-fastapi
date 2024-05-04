import uuid

from fastapi import APIRouter, Depends, HTTPException
from app.services.database import get_db
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import ModelList, ProcessedImagesSchema, ModelSchema, ProcessedImagesList
from ..models import ProcessedImages, Models
from ..models import User as UserModel
from app.deps import get_current_user

model_router = APIRouter(prefix="/model", tags=["model"])


@model_router.get("/get-models", response_model=ModelList)
async def get_models(db: AsyncSession = Depends(get_db), check_user: UserModel = Depends(get_current_user)):
    if not check_user:
        raise HTTPException(
            check_user
        )
    models = await Models.get_all(db)
    return {"models": [ModelSchema.model_validate(model) for model in models]}


@model_router.get("/get-pims", response_model=ProcessedImagesList)
async def get_pims(user_id: uuid.UUID, db: AsyncSession = Depends(get_db), check_user: UserModel = Depends(get_current_user)):
    if not check_user:
        raise HTTPException(
            check_user
        )
    pims = await ProcessedImages.get_by_user_id(db,user_id)
    return {"pims": [ProcessedImagesSchema.model_validate(pim) for pim in pims]}
