# chat/routing.py
from django.urls import path
from hlo.consumers import *
from . import consumers

websocket_urlpatterns = [
    # re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    path("ws/test/", TestConsumer.as_asgi())
]