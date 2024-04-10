from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from typing import Annotated

class Item(BaseModel):
    name: str
    description: str|None = None
    price: float
    tax: float|None = None

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(item_id: Annotated[int, Path(title="The ID of the item", ge=3)], q: Annotated[str|None, Query()] = None):
    """
    Path parameter with specific conditions for valid argument
    """
    results = {"items_id": item_id}
    if q:
        results.update({"q":q})
    return results