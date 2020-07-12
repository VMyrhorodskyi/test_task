import uuid
from django.db import models

SIDE_CHOICES = [
    ("Buy", "Buy"),
    ("Sell", "Sell"),
]


class Account(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    api_key = models.CharField(max_length=24, unique=True)
    api_secret = models.CharField(max_length=48, unique=True)


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    symbol = models.CharField(max_length=6)
    volume = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    side = models.CharField(choices=SIDE_CHOICES, max_length=4)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
