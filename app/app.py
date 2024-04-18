from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Any, Union

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": item_id}


class UnicornException(Exception):
    def __init__(self, name: str) -> None:
        self.name = name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    """
    Define how the UnicornException will be handled
    """
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something."}
    )

@app.get("/unicorn/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}