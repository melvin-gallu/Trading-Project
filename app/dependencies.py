from typing import Annotated

from fastapi import Header, HTTPException, status

async def get_token_header(x_token: Annotated[str|None, Header()]):
    if x_token != "fake-secret-token":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid X-Token header")
    
async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No jessica token provided")
    
