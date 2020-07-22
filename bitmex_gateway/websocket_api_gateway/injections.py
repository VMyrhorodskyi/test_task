import injector

from .bitmex_ws import BitmexWSConnectionPool


class BitmexWSModule(injector.Module):
    @injector.provider
    @injector.singleton
    def provide_bitmex_ws_connection_pool(self) -> BitmexWSConnectionPool:
        return BitmexWSConnectionPool()


class WSMetaModule(injector.Module):
    def configure(self, binder: injector.Binder) -> None:
        binder.install(BitmexWSModule)
