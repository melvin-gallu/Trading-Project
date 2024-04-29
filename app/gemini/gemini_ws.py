from fastapi import APIRouter, WebSocket, WebSocketDisconnect, WebSocketException, status
from fastapi.responses import HTMLResponse
from typing import Annotated

import asyncio

from .GeminiSocketManager import GeminiSocketManager

router = APIRouter(
    prefix="/gemini",
    tags=["ws"]
)

external_ws_client = GeminiSocketManager()

@router.websocket("/market-data")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            await external_ws_client.connect()
            async for data in external_ws_client.listen():
                clean_data = await external_ws_client.clean_data(data=data)
                await ws.send_json(clean_data)
    except WebSocketDisconnect:
        print(f"Websocket connection closed cleanly")
    except Exception as e:
        print(f"Websocket error : {e}")
    finally:
        ws.close()