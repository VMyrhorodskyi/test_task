import json
import websockets
from django.conf import settings


class BitmexWSConnection:
    def __init__(self, account_name):
        self.account_name = account_name

    async def check_bitmex_message(self, message):
        return (
            message.get("action") == "update"
            and "data" in message
            and "lastPrice" in message["data"][0]
        )

    async def parse_bitmex_message(self, message):
        message_data = message["data"][0]
        return {
            "account": self.account_name,
            "symbol": message_data["symbol"],
            "price": message_data["lastPrice"],
            "timestamp": message_data["timestamp"],
        }

    async def subscribe_bitmex(self):
        async with websockets.connect(settings.BITMEX_WS_URL) as bitmex_ws:
            await bitmex_ws.send(json.dumps({"op": "subscribe", "args": "instrument"}))
            async with websockets.connect(settings.WS_URL) as ws:
                while True:
                    message = json.loads(await bitmex_ws.recv())
                    if await self.check_bitmex_message(message=message):
                        await ws.send(
                            json.dumps(await self.parse_bitmex_message(message=message))
                        )


class BitmexWSConnectionPool:
    def __init__(self):
        self.connections = {}

    def get(self, account_name):
        return self.connections.get(account_name)

    def update(self, account_name, connection):
        self.connections[account_name] = connection
