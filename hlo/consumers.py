from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):
    
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_name, self.room_group_name
        )

        self.accept()
        self.send(text_data=json.dumps({
            "status" :  "connected"
        }))
    

    def receive(self, text_data):
        print(text_data)
        async_to_sync(self.channel_layer.group_send)(
            "chat",
            {
                "type": "chat.message",
                "text": text_data,
            },
        )
        
    

    def disconnect(self):
        pass
