import json
from channels.generic.websocket import WebsocketConsumer
from django.conf import settings
from threading import Thread
from websocket import WebSocketApp


class QuotesConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bitmex_ws = WebSocketApp(
            settings.BITMEX_WS_URL, on_message=self.on_bitmex_message
        )

        self.bitmex_ws_thread = Thread(target=lambda: self.bitmex_ws.run_forever())
        self.bitmex_ws_thread.daemon = True
        self.bitmex_ws_thread.start()

    def on_bitmex_message(self, message):
        message = json.loads(message)
        if self.check_bitmex_message(message=message):
            self.send(json.dumps(self.parse_bitmex_message(message)))

    def check_bitmex_message(self, message):
        return (
            message.get("action") == "update"
            and "data" in message
            and "lastPrice" in message["data"][0]
        )

    def parse_bitmex_message(self, message):
        message_data = message["data"][0]
        return {
            "account": self.account_name,
            "symbol": message_data["symbol"],
            "price": message_data["lastPrice"],
            "timestamp": message_data["timestamp"],
        }

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)

        if text_data_json.get("action") == "subscribe" and text_data_json.get(
            "account"
        ):
            self.account_name = text_data_json["account"]
            self.bitmex_ws.send(
                json.dumps({"op": "subscribe", "args": settings.BITMEX_WS_SUBSCRIPTION})
            )
        if text_data_json.get("action") == "unsubscribe" and text_data_json.get(
            "account"
        ):
            self.account_name = None
            self.bitmex_ws.send(
                json.dumps(
                    {"op": "unsubscribe", "args": settings.BITMEX_WS_SUBSCRIPTION}
                )
            )
