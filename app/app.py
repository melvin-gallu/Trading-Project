from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Any

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

class UserIn(BaseModel):
    username: str
    pwd: str
    email: Annotated[EmailStr, Field(title="email type")]
    full_name : str|None = None

class UserOut(BaseModel):
    username: str
    email: Annotated[EmailStr, Field(title="email type")]
    full_name: str|None = None

@app.post("/items/", response_model=Item)
async def create_items(item: Item) -> Any:
    """
    Define the returned data type with flexibility
    """
    return item

@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 320.0}
    ]

@app.post("/users/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user