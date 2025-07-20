# chats/serializers.py

from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "bio", "avatar"]


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)  # include sender details

    class Meta:
        model = Message
        fields = ["id", "conversation", "sender", "content", "timestamp"]
        read_only_fields = ["id", "timestamp", "sender", "conversation"]


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True, source="messages.all")

    class Meta:
        model = Conversation
        fields = ["id", "participants", "messages", "created_at"]
