from fastapi import Depends, FastAPI
from fastapi.security.api_key import APIKey
from main import openai_answers
from typing import Union

import auth

app = FastAPI()

@app.post('/send')
def send_question(message, api_key: APIKey = Depends(auth.get_api_key)):
    if message:
        answer = openai_answers(message)
    return {'message':answer}