from fastapi import APIRouter, Depends
from app.services.database import get_db

from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import ModelList
from ..models import ProcessedImages, Models

model_router = APIRouter(prefix="/model", tags=["model"])


@model_router.get("/get-models", response_model=ModelList)
async def get_models(db: AsyncSession = Depends(get_db)):
    models = await Models.get_all(db)
    return {"models": models}
