from rest_framework import serializers

from .models import Account, Order


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ("url", "name", "api_key", "api_secret")


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    bitmex_id = serializers.UUIDField()

    class Meta:
        model = Order
        fields = (
            "url",
            "order_id",
            "bitmex_id",
            "symbol",
            "volume",
            "timestamp",
            "side",
            "price",
            "account",
        )
