from datetime import datetime
from typing import List
import uuid
from pydantic import BaseModel, EmailStr, constr


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: EmailStr

    class Config:
        orm_mode = True

class UserResponse(UserBaseSchema):
    id: uuid.UUID
    time_created: datetime
    time_updated: datetime