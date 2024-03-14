from rest_framework import serializers
from app.player.models.selected_player import SelectedPlayer
from app.player.models.player import Player
import random

class SelectedPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedPlayer
        fields = '__all__'

    def to_internal_value(self, data):
        if 'player' not in data or data['player'] is None:
            all_players = Player.objects.all()
            random_player = random.choice(all_players)
            data['player'] = random_player.id
        
        return super().to_internal_value(data)
