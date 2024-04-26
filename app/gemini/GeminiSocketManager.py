import asyncio
import websockets
import ssl
from typing import Annotated

class GeminiSocketManager():
    def __init__(self) -> None:
        self.ws_base_endpoint = "wss://api.sandbox.gemini.com/v1/"
        self.connected_clients = set()

    async def connect(self, pair: str = "BTCUSD"):
        uri = self.ws_base_endpoint + "marketdata/" + pair
        ssl_context = ssl.create_default_context()
        self.websocket = await websockets.connect(uri=uri, ssl=ssl_context)
        await self.listen()

    async def listen(self):
        try:
            while True:
                data = await self.websocket.recv()
                for client in self.connected_clients:
                    await client.send_text(data)
        except websockets.ConnectionClosedError:
            self.websocket = None
            print("Connection to external WebScoket server closed.")
