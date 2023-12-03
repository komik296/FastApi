from fastapi import FastAPI

from models.models import User


app = FastAPI()


user = User(name='Johon Doe', id=1)


@app.get('/')
async def rout():
    return {'message': 'Hello World!'}


@app.get('/users')
async def users():
    return user