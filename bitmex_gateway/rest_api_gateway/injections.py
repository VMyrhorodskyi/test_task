import injector
from bitmex import bitmex
from django.conf import settings

from .bitmex_api import BitmexOrders
from .typings import BitmexClient


class BitmexModule(injector.Module):
    @injector.provider
    @injector.singleton
    def provide_bitmex_client(self) -> BitmexClient:
        return bitmex(
            test=True,
            api_key=settings.DEFAULT_ACCOUNT_API_KEY,
            api_secret=settings.DEFAULT_ACCOUNT_API_SECRET,
        )

    def configure(self, binder: injector.Binder) -> None:
        binder.bind(
            BitmexOrders, to=BitmexOrders, scope=injector.SingletonScope,
        )


class MetaModule(injector.Module):
    def configure(self, binder: injector.Binder) -> None:
        binder.install(BitmexModule)
