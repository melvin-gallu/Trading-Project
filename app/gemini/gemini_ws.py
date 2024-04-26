from fastapi import APIRouter, WebSocket, WebSocketDisconnect, WebSocketException, status
from fastapi.responses import HTMLResponse
from typing import Annotated

import asyncio

from .GeminiSocketManager import GeminiSocketManager

router = APIRouter(
    prefix="/ws",
    tags=["ws"]
)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>External WebSocket Data</title>
</head>
<body>
    <h1>Hello</h1>
    <div id="messages"></div>

    <script>
        const ws = new WebSocket("ws://localhost:8000/ws");

        ws.onopen = () => {
            console.log("WebSocket connection established.");
        };

        ws.onmessage = (event) => {
            const messagesDiv = document.getElementById("messages");
            messagesDiv.innerHTML += `<p>${event.data}</p>`;
        };

        ws.onerror = (error) => {
            console.error(`WebSocket error: ${error}`);
        };

        ws.onclose = () => {
            console.log("WebSocket connection closed.");
        };
    </script>
</body>
</html>
"""


external_ws_client = GeminiSocketManager()

@router.websocket("/")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        data = {"message": "hello"}
        await ws.send_text(f"Message text was: {data}")

@router.get("/")
async def get():
    return HTMLResponse(html_content)