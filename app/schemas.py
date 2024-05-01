import uuid
from pydantic import BaseModel

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
