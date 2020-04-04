from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from .token_auth import TokenAuthMiddlewareStack

from . import consumers

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': TokenAuthMiddlewareStack(
        URLRouter(
            [
                path('test', consumers.ChatConsumer),
            ]
        )
    ),
})