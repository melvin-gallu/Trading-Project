from datetime import datetime

from fastapi import FastAPI, Path, Body, Depends
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

async def common_parameters(q: str|None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

CommonsDep = Annotated[dict, Depends(common_parameters)]

class CommonQueryParams:
    def __init__(self, q: str|None = None, skip: int = 0, limit: int = 100) -> None:
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get("/items/")
async def read_items(commons: CommonsDep):
    """
    Uses dependency and alias
    This is in partice used when you need to have a lot of times the same dependencies on parameters accross various path
    """
    return commons

@app.get("/users/")
async def read_users(commons: CommonsDep):
    return commons

@app.get("/items/class")
async def read_items_class(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    """
    Uses a class as dependency
    """
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    response.update({"items": commons.skip + commons.limit})
    return response

