from fastapi import FastAPI

from models.feedback import Feedback


app = FastAPI()

data = []

@app.get('/feedback')
async def feedback_data(feedback: Feedback):
    data.append(feedback)
    return {'message': f'Data is available. Thank you {feedback.name}'}