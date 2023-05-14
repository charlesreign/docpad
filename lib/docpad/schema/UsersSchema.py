from pydantic import BaseModel, EmailStr, constr

class User(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    role: str = 'user'
    email: EmailStr
    password: constr(min_length=8)

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: constr(min_length=8)