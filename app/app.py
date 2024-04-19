from datetime import datetime

from fastapi import FastAPI, Path, Body, Depends, Cookie, Header, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Annotated



async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    
async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key
    
app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)]) #add global dependecies to the whole app
