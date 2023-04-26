from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from APIs.serializers import *
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

class ChatRoomAPIView(APIView):
    def post(self, request):
        serializer = ChatRoomSerializer(data=request.data)
        if serializer.is_valid():
            chat_room = ChatRoom.objects.create(name=serializer.validated_data['name'])
            participants = serializer.validated_data['participants']
            for participant_id in participants:
                participant = get_object_or_404(User, id=participant_id)
                chat_room.participants.add(participant)
            chat_room.save()
            return Response(ChatRoomSerializer(chat_room).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChatRoomWebSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        chat_room_id = self.scope['url_route']['kwargs']['chat_room_id']
        self.chat_room = get_object_or_404(ChatRoom, id=chat_room_id)
        self.room_group_name = f'chat_room_{self.chat_room.id}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json['message']
        author = self.scope['user']
        message = Message.objects.create(
            chat_room=self.chat_room,
            author=author,
            content=message_content
        )
        message_serializer = ChatRoomMessageSerializer({
            'chat_room': ChatRoomSerializer(self.chat_room).data,
            'message': MessageSerializer(message).data
        })
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_room_message',
                'message': message_serializer.data
            }
        )

    async def chat_room_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))