from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://localhost:8080",
    "http://localhost"
]

#Add the different parameters needed for the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, #can yuse allow_origin_regex to define regex string to match against origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def main():
    return {"message": "Hello World"}