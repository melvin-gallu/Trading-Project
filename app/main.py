from fastapi import FastAPI, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .dependencies import get_query_token, get_token_header
from .routeurs import items, users
from .internal import admin
from .websocketbackend import stream


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

#Include the router in the main FastAPI app
app.include_router(users.router)
app.include_router(items.router)
app.include_router(stream.router)
#Set up custom prefix, tags, dependencies for an already predefined route
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_query_token)],
    responses={418: {"description": "I'm a teapot"}}
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

def write_notification(email: str, message: str = ""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    """
    The write notification function will be run after the response is sent 
    """
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}