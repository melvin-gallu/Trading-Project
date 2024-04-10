from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

@app.get("/items/")
async def read_items(ads_id: Annotated[str|None, Cookie()] = None):
    """"
    Cookie Parameter
    """
    return {"ads_id": ads_id}

@app.get("/items/headers")
async def read_items_headers(user_agent: Annotated[str|None, Header()] = None):
    """
    Header Parameter
    """
    return {"User-Agent": user_agent}

@app.get("/items/headers/bis")
async def read_items_headers_bis(x_token: Annotated[list[str]|None, Header()] = None):
    """
    Header with multiple parameters
    """
    return {"X-Token values": x_token}

