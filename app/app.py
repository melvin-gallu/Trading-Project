from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated

class Item(BaseModel):
    name: str
    description: str|None = None
    price: float
    tax: float|None = None

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str|None, Query(max_length=50)] = None):
    """
    Specifiy condition for validation using annotated query parameter
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q":q})
    return results

@app.get("/items/bis/")
async def read_items(q: Annotated[str|None, Query(min_length=3,max_length=50,pattern="^fixedquery$")] = None):
    """
    Specify a regex expression to use in the annotated query parameter
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q":q})
    return results

@app.get("/items/tris/")
async def read_items(q: Annotated[str, Query(min_length=3,max_length=50)]):
    """
    Make query parameter required
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q":q})
    return results
@app.get("/items/list/")
async def read_items_list(q: Annotated[list[str]|None, Query()] = ["Mel","vin"]):
    """
    Query parameter defined as a list of string
    Call it via /items/list/?q=item1&q=item2
    """
    query_items = {"q": q}
    return query_items