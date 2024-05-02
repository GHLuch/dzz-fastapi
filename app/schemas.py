import uuid
from pydantic import BaseModel
import datetime

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

class AIModel(BaseModel):
    id: uuid.UUID
    name: str


class ModelList(BaseModel):
    models: list[AIModel]


class ProcessedImagesSchema(BaseModel):
    id: uuid.UUID
    user_id: int
    model_id: int
    hesh_img: str
    url_img: int
    create_time: datetime.datetime

class ProcessedImagesList(BaseModel):
    pims: list[ProcessedImagesSchema]