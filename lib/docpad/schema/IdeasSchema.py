import uuid
from pydantic import BaseModel, EmailStr, constr


class Idea(BaseModel):
    title:str
    content:str
    category:str
    image:str
    user_id: uuid.UUID | None = None

    class Config:
        orm_mode = True