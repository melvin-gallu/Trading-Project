from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str|None = None

app = FastAPI()

@app.put("/items/{id}")
async def update_item(id: str, item: Item):
    """
    Convert a Pydantic model to a dict, and the datetime to a str, to suit the database needs
    """
    json_comaptible_item_data = jsonable_encoder(item)
    fake_db[id] = json_comaptible_item_data
    return {"db": fake_db}