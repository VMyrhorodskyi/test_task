from django_filters.rest_framework import DjangoFilterBackend
from django_injector import inject
from rest_framework.viewsets import ModelViewSet

from .bitmex_api import BitmexOrders
from .models import Account, Order
from .serializers import (
    AccountSerializer,
    OrderSerializer,
)


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["account"]

    @inject
    def __init__(self, bitmex_orders: BitmexOrders, **kwargs):
        super().__init__(**kwargs)
        self.bitmex_orders = bitmex_orders

    def create(self, request, *args, **kwargs):
        self.bitmex_orders.post(data=request.data)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        raise NotImplementedError(self.__class__.__name__)

    def destroy(self, request, *args, **kwargs):
        self.bitmex_orders.delete(order_id=kwargs["pk"])
        return super().destroy(self, request, *args, **kwargs)
