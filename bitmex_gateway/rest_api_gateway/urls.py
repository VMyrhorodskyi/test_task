from django.urls import include, path
from rest_framework import routers

from .views import AccountViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r"accounts", AccountViewSet)
router.register(r"orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
