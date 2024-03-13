from rest_framework import generics
from rest_framework.response import Response
from app.player.models.selected_player import SelectedPlayer
from app.player.serializers.selected_player import SelectedPlayerSerializer
from datetime import datetime, timezone

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
