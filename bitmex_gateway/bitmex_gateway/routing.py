from channels.routing import ProtocolTypeRouter, URLRouter

import websocket_api_gateway.routing

application = ProtocolTypeRouter(
    {"websocket": URLRouter(websocket_api_gateway.routing.websocket_urlpatterns)}
)
