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

@router.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    external_ws_client.connected_clients.add(ws)
    try:
        while True:
            data = await external_ws_client.connect()
            await ws.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        print(f"Websocket connection closed cleanly")
    except Exception as e:
        print(f"Websocket error : {e}")
    finally:
        external_ws_client.connected_clients.remove(ws)