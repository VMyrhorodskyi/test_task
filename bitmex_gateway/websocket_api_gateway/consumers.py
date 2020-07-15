import json
from bitmex_websocket import Instrument
from bitmex_websocket.constants import InstrumentChannels
from channels.generic.websocket import WebsocketConsumer


class QuotesConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bitmex_ws_client = Instrument(channels=[InstrumentChannels.quote])

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        if self.bitmex_ws_client.is_connected():
            self.bitmex_ws_client.close()

    def prepare_response(self, account_name, bitmex_message):
        last_quote_data = bitmex_message["data"][-1]

        return json.dumps(
            {
                "timestamp": last_quote_data["timestamp"],
                "account": account_name,
                "symbol": last_quote_data["symbol"],
                "price": last_quote_data["askPrice"],
            }
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)

        if text_data_json.get("action") == "subscribe" and text_data_json.get(
            "account"
        ):
            self.bitmex_ws_client.on(
                "action",
                lambda message: self.send(
                    self.prepare_response(
                        account_name=text_data_json["account"], bitmex_message=message
                    )
                ),
            )
            self.bitmex_ws_client.run_forever()
