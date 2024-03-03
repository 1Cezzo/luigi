from rest_framework import serializers
from app.player.models.player import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'age', 'nationality', 'team_name', 'team_logo', 'player_image']