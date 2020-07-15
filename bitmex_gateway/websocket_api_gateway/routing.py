from django.urls import re_path

from .consumers import QuotesConsumer

websocket_urlpatterns = [
    re_path(r"^ws/quotes/$", QuotesConsumer),
]
