from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    username: str


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}

@router.post("/users/", tags=["users"])
async def create_user(user: User) -> list[User]:
    return user