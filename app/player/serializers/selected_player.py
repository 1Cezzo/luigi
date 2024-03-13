from rest_framework import serializers
from app.player.models.selected_player import SelectedPlayer

class SelectedPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedPlayer
        fields = '__all__'
