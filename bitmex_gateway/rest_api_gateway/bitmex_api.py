from django.conf import settings
from django_injector import inject

from .typings import BitmexClient


class BitmexOrders:
    @inject
    def __init__(self, bitmex_client: BitmexClient):
        self.bitmex_client = bitmex_client

    def post(self, data):
        return self.bitmex_client.Order.Order_new(
            ordType=settings.BITMEX_API_ORDERS_DEFAULT_TYPE,
            symbol=data["symbol"],
            orderQty=data["volume"],
            side=data["side"],
        ).result()

    def delete(self, order_id):
        return self.bitmex_client.Order.Order_cancel(orderID=order_id).result()
