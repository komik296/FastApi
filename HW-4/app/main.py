from fastapi import FastAPI

from models.model import User
from services.correct_age import more_than_eighteen

app = FastAPI()


@app.get('/')
async def route():
    return {'message': 'You are the best!'}


@app.post('/user')
async def users(user: User):
    dict_user = dict(user)
    dict_user['is_adult'] = more_than_eighteen(user.age)
    return dict_user