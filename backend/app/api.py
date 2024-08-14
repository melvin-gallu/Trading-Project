from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

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
    price: float
    tax: float | None = None

@router.post('/items')
async def create_item(item: Item):
    item_dict = item.model_dump()
    print(item_dict)
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax':price_with_tax})
    return item_dict