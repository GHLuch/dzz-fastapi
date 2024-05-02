from fastapi import APIRouter, Depends
from app.services.database import get_db

from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import ModelList, ProcessedImagesSchema, ModelSchema, ProcessedImagesList
from ..models import ProcessedImages, Models

model_router = APIRouter(prefix="/model", tags=["model"])


@model_router.get("/get-models", response_model=ModelList)
async def get_models(db: AsyncSession = Depends(get_db)):
    models = await Models.get_all(db)
    return {"models": [ModelSchema.model_validate(model) for model in models]}


@model_router.get("/get-pims", response_model=ProcessedImagesList)
async def get_pims(db: AsyncSession = Depends(get_db)):
    pims = await ProcessedImages.get_by_user_id(db)
    return {"pims": [ProcessedImagesSchema.model_validate(pim) for pim in pims]}
