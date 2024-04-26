import asyncio
import websockets
import ssl
from typing import Annotated

class GeminiSocketManager():
    def __init__(self) -> None:
        self.ws_base_endpoint = "wss://api.sandbox.gemini.com/v1/"
        self.connected_clients = set()
        self.websocket = None

    def connect(self, pair: str = "BTCUSD"):
        uri = self.ws_base_endpoint + "marketdata/" + pair
        self.websocket = client.connect(uri=uri)
        self.listen()

    def listen(self):
        try:
            while True:
                data = self.websocket.recv()
                print(data)
                # for client in self.connected_clients:
                #     client.send_text(data)
        except websockets.ConnectionClosedError:
            self.websocket = None
            print("Connection to external WebScoket server closed.")

    def start(self):
        self.connect()

external_ws_client = GeminiSocketManager()
external_ws_client.connect()