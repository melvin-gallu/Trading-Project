from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field
from typing import Annotated


class Image(BaseModel):
    url: str
    name: str|None = None

class Item(BaseModel):
    name: str
    description: str|None = Field(default=None, title="Description of the item", max_length=300)
    price: float = Field(gt=0)
    tax: float|None = None
    tags: list[int] = []
    tags_unique: set[int] = set() #set contains only unique values
    image: Image|None = None #nest another class in *this

app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id: Annotated[int|None, Path(lt=100)], 
                      item: Item|None = None):
    """
    Body parameter with nested list inside the class
    """
    results = {"item_id": item_id, "item": item}
    return results

