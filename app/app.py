from fastapi import FastAPI, Query, Path, Body, Cookie, Header, status
from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Any, Union

app = FastAPI()

@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}
