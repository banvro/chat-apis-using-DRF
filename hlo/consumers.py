from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TestConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        await (self.channel_layer.group_add)(
            self.room_name, self.room_group_name
        )

        await self.accept()
        await self.send(text_data=json.dumps({
            "status" :  "connected"
        }))
    

    async def receive(self, text_data):
        print(text_data)
        await (self.channel_layer.group_send)(
            "chat",
            {
                "type": "chat.message",
                "text": text_data,
            },
        )
        
    

    async def disconnect(self):
        pass
