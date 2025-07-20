# chats/views.py

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        return self.queryset.filter(participants=self.request.user)

    def perform_create(self, serializer):
        conversation = serializer.save()
        conversation.participants.add(self.request.user)
        conversation.save()

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def add_participant(self, request, pk=None):
        conversation = self.get_object()
        user_id = request.data.get("user_id")

        if user_id:
            from .models import User

            user = get_object_or_404(User, id=user_id)
            conversation.participants.add(user)
            return Response({"status": "participant added"})
        return Response({"error": "user_id required"}, status=status.HTTP_400_BAD_REQUEST)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        return self.queryset.filter(conversation__participants=self.request.user)

    def perform_create(self, serializer):
        conversation_id = self.request.data.get("conversation")
        if not conversation_id:
            return Response({"error": "conversation ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        conversation = get_object_or_404(Conversation, id=conversation_id)

        if self.request.user not in conversation.participants.all():
            return Response(
                {"error": "You are not a participant in this conversation."}, status=status.HTTP_403_FORBIDDEN
            )

        serializer.save(sender=self.request.user, conversation=conversation)
