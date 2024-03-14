from rest_framework import generics
from rest_framework.response import Response
from app.player.models.selected_player import SelectedPlayer
from app.player.serializers.selected_player import SelectedPlayerSerializer
from app.player.models.player import Player
from datetime import datetime, timezone
from rest_framework import status
import random

class SelectedPlayerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SelectedPlayer.objects.all()
    serializer_class = SelectedPlayerSerializer

class FetchSelectedPlayerAPIView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        today = datetime.now(timezone.utc).date()

        try:
            selected_player = SelectedPlayer.objects.get(date=today)
            serializer = SelectedPlayerSerializer(selected_player)
            return Response(serializer.data)
        except SelectedPlayer.DoesNotExist:
            return Response({'error': 'Selected player not found for today'}, status=404)

class CreateSelectedPlayerAPIView(generics.CreateAPIView):
    serializer_class = SelectedPlayerSerializer

    def create(self, request, *args, **kwargs):
        players = Player.objects.all()
        selected_player = random.choice(players)
        selected_player_instance = SelectedPlayer.objects.create(player=selected_player)
        serializer = self.get_serializer(selected_player_instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

