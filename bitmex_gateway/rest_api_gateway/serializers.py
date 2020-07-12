from rest_framework import serializers

from .models import Account, Order


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ("url", "name", "api_key", "api_secret")


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = (
            "url",
            "symbol",
            "volume",
            "timestamp",
            "side",
            "price",
            "account",
        )
