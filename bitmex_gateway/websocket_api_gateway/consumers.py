import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django_injector import inject

from .bitmex_ws import BitmexWSConnection, BitmexWSConnectionPool


class Consumer(AsyncWebsocketConsumer):
    @inject
    def __init__(
        self, bitmex_ws_connection_pool: BitmexWSConnectionPool, *args, **kwargs
    ):
        super().__init__(self, *args, **kwargs)

        self.bitmex_ws_connection_pool = bitmex_ws_connection_pool

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)

        if text_data_json.get("action") == "subscribe" and text_data_json.get(
            "account"
        ):
            await self.channel_layer.group_add(
                text_data_json["account"], self.channel_name
            )

            if not self.bitmex_ws_connection_pool.get(text_data_json["account"]):
                connection = BitmexWSConnection(account_name=text_data_json["account"])
                self.bitmex_ws_connection_pool.update(
                    account_name=text_data_json["account"], connection=connection
                )

                asyncio.get_event_loop().create_task(connection.subscribe_bitmex())
        if text_data_json.get("action") == "unsubscribe" and text_data_json.get(
            "account"
        ):
            await self.channel_layer.group_discard(
                text_data_json["account"], self.channel_name
            )

        if not text_data_json.get("action") and text_data_json.get("account"):
            await self.channel_layer.group_send(
                text_data_json["account"],
                {"type": "group_message", "message": text_data},
            )

    async def group_message(self, event):
        await self.send(text_data=event["message"])
