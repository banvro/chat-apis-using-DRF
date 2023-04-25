# urls.py
from django.urls import path
from .views import ChatRoomAPIView, ChatRoomWebSocketConsumer

urlpatterns = [
    path('chat_rooms/', ChatRoomAPIView.as_view()),
    path('chat_rooms/<int:chat_room_id>/', ChatRoomWebSocketConsumer.as_asgi()),
]
