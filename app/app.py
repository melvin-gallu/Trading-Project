from datetime import datetime

from fastapi import FastAPI, Path, Body
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Annotated

class Item(BaseModel):
    name: str|None = None
    description: str|None = None
    price: float|None = None
    tax: float = 10.5
    tags: list[str] = []

app = FastAPI()

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/items/{id}")
async def read_item(id: Annotated[str|None, Path()]):
    return items[id]


@app.patch("/items/{id}", response_model=Item)
async def udpdate_item(id: Annotated[str|None, Path()], item: Annotated[Item, Body()]):
    """
    Update partially an item using **exclude_unset**
    """
    stored_item_data = items[id] #retrieved stored data
    stored_item_model = Item(**stored_item_data) #convert data t Pydantic model
    udpdate_data = item.model_dump(exclude_unset=True) #generate dict without default values from input model
    updated_item = stored_item_model.model_copy(update=udpdate_data) #create a copy of stored model, update its attributes with received partial updates
    items[id] = jsonable_encoder(updated_item) #convert the copied model to something that can be stored in a DB
    return updated_item