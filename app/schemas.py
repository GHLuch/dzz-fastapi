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

class ModelSchema(BaseModel):
    id: uuid.UUID
    name: str

    def model_validate(self):
        return self

    class Config:
        orm_mode = True

class ModelList(BaseModel):
    models: list[ModelSchema]


class ProcessedImagesSchema(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    model_id: uuid.UUID
    hesh_img: str
    url_img: str
    create_time: datetime.datetime

    def model_validate(self):
        return self
    
    class Config:
        orm_mode = True

class ProcessedImagesList(BaseModel):
    pims: list[ProcessedImagesSchema]