from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field
from typing import Annotated

class Item(BaseModel):
    name: str
    description: str|None = Field(default=None, title="Description of the item", max_length=300)
    price: float = Field(gt=0)
    tax: float|None = None

class User(BaseModel):
    username: str
    full_name: str|None = None

app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id: Annotated[int|None, Path(lt=100)], 
                      q: Annotated[str|None, Query()] = None,
                      item: Item|None = None, user: User|None = None,
                      importance: Annotated[int, Body(le=5)] = 5):
    """
    Path parameter + query parameter + multiple body parameters
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})
    return results

