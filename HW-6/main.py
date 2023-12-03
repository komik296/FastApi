from fastapi import FastAPI
from pydantic import BaseModel, PositiveInt, EmailStr

app = FastAPI()


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: None | PositiveInt = None
    is_subscribed: bool = False



@app.post('/create_user')
async def create_user(user: UserCreate):
    return user
