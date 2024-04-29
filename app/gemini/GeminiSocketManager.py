import asyncio
import websockets
import ssl
from typing import Annotated
import json

class GeminiSocketManager():
    def __init__(self) -> None:
        self.ws_base_endpoint = "wss://api.sandbox.gemini.com/v1/"

    async def connect(self, pair: str = "BTCUSD"):
        uri = self.ws_base_endpoint + "marketdata/" + pair
        ssl_context = ssl.create_default_context()
        self.websocket = await websockets.connect(uri=uri, ssl=ssl_context)
        self.first_message = False

    async def listen(self):
        try:
            while True:
                data = await self.websocket.recv()
                yield data
        except websockets.ConnectionClosedError:
            self.websocket = None
            print("Connection to external WebScoket server closed.")

    async def clean_data(self,data):
        try:
            data = json.loads(data)
            data = data["events"]
            if not self.first_message:
                data = [{"price":item["price"], "remaining":item["remaining"]} for item in data]
                self.first_message = True
            return data
        except Exception as e:
            raise e