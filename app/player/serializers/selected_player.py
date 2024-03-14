from rest_framework import serializers
from app.player.models.selected_player import SelectedPlayer
from app.player.models.player import Player
import random

class SelectedPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedPlayer
        fields = '__all__'

    def create(self, validated_data):
        # If "player" is not provided in the validated_data, select a random player
        if 'player' not in validated_data:
            all_players = Player.objects.all()
            random_player = random.choice(all_players)
            validated_data['player'] = random_player
        
        return super().create(validated_data)
