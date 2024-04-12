from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Any, Union

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

class BaseUser(BaseModel):
    username: str
    email: Annotated[EmailStr, Field(title="email type")]
    full_name: str|None = None

class UserIn(BaseUser):
    pwd: str

class UserInDB(BaseUser):
    hashed_pwd: str

class BaseVehicle(BaseModel):
    description: str
    type: str

class Car(BaseVehicle):
    type: str = "car"

class Plane(BaseVehicle):
    type: str = "plane"
    size: int

def fake_pwd_hasher(pwd: str):
    return "secret" + pwd

def fake_save_user(user_in: UserIn):
    hashed_pwd= fake_pwd_hasher(user_in.pwd)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_pwd=hashed_pwd) #** is using to unwrap the dict and pass the keys and values as key-value arguments
    print("User saved!")
    return user_in_db

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

@app.post("/users/", response_model=BaseUser)
async def create_user(user: UserIn) -> Any:
    return user

@app.post("/users/db/", response_model=BaseUser)
async def create_user_in_db(user: UserIn) -> Any:
    user_saved = fake_save_user(user_in=user)
    return user_saved

items = {
    "car": {
        "description": "4 wheel driving machine",
        "type": "car"
    },
    "plane":
    {
        "description": "Flies in the sky",
        "type": "plane",
        "size": 5
    }
}

@app.get("/vehicle/{typeVehicle}",response_model=Union[Plane, Car])
async def read_vehicle(typeVehicle: str):
    return items[typeVehicle]