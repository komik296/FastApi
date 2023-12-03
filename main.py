from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/custom")
async def read_custom_meessage():
    return {"message": "This is a custom message!"}


#uvicorn main:app --reload