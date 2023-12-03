from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()


class User(BaseModel):
    username: str
    message: str


@app.post('/')
async def root(user: User):

    print(f'Мы получили от {user.username} сообщение с текстом {user.message}')

    return user




