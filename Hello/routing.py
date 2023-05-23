import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path, re_path

from hlo.consumers import TestConsumer

from django.core.asgi import get_asgi_application

# application = ProtocolTypeRouter({
#     'websocket': AllowedHostsOriginValidator
#     (AuthMiddlewareStack(
#         URLRouter([
#             path('ws/test/', TestConsumer),
#         ])
#     )
#     ),
# })
 

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path(r'ws/test/', TestConsumer.as_asgi()),
            ])
        )
    ),
})