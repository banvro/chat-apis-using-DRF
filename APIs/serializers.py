# from rest_framework import serializers
# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username']

# class ChatRoomSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     participants = serializers.ListField(child=serializers.IntegerField())

# class MessageSerializer(serializers.Serializer):
#     author = UserSerializer()
#     content = serializers.CharField()
#     timestamp = serializers.DateTimeField()

# class ChatRoomMessageSerializer(serializers.Serializer):
#     chat_room = ChatRoomSerializer()
#     message = MessageSerializer()