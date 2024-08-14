from fastapi import APIRouter, HTTPException, Body, Form
from pydantic import BaseModel, Field
from typing import Annotated

router = APIRouter(
    prefix="/api/v1",
    tags=["api/v1"],
    responses={404: {"description":"Not found"}}
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}

@router.get("/db/{db_item_id}")
async def read_name(db_item_id: str):
    if db_item_id not in fake_items_db:
        raise HTTPException(
            status_code=404, detail="Item not found"
        )
    return {'name': fake_items_db[db_item_id]['name'], 'db_item_id':db_item_id}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float = Field(gt=0,description='Price must be greater than 0')
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str

@router.post('/items')
async def create_item(item: Item, user: User, importance: Annotated[int, Body()]) -> dict: #use pydantic model (or Body for singular value) so that fastAPI understand it is a body request
    print(item, user)
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax':price_with_tax})

    print(item_dict)
    result = {'item': item, 'user': user, 'importance':importance}
    return result

@router.post('/form/test')
async def form_operation(user:User) -> dict:
    print(user.model_dump())
    result = user.model_dump()
    return result