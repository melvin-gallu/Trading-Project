from fastapi import FastAPI, Query, Path, Body, Cookie, Header, status, Form
from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Any, Union

app = FastAPI()

@app.post("/login/")
async def login(username: Annotated[str, Form()], pwd: Annotated[str, Form()]):
    """
    The way HTML forms sends the data to the server normally uses a "special" encoding for that data, 
    it's different from JSON.
    """
    return {"username": username}