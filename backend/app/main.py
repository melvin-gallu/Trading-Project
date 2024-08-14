from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import api

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api.router)

@app.get('/', tags=["root"])
async def home() -> dict:
    return {'message':'hello world from fastapi app'}

@app.get('/test', tags=["root"])
async def test() -> dict:
    json = {
        'message': {
            'test':'test message',
            'test2':'second test message'
        }
    }
    return json