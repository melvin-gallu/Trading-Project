from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .dependencies import get_query_token, get_token_header
from .routeurs import items, users
from .internal import admin

app = FastAPI(dependencies=[Depends(get_query_token)])

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
#Set up custom prefix, tags, dependencies for an already predefined route
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}}
)

@app.get("/")
async def root():
    return {"message": "Hello World"}