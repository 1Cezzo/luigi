import requests
from django.core.management.base import BaseCommand
from app.player.models.selected_player import SelectedPlayer
from datetime import datetime, timezone
from random import choice

class Command(BaseCommand):
    help = 'Selects a new player for the current day'

    def handle(self, *args, **options):
        today = datetime.now(timezone.utc).date()

        try:
            previous_selected_player_instance = SelectedPlayer.objects.get(date=today)
            previous_selected_player_id = previous_selected_player_instance.player_id
        except SelectedPlayer.DoesNotExist:
            previous_selected_player_id = None

        url = 'https://luigi-backend-7f709e978d15.herokuapp.com/players/'
        response = requests.get(url)
        response.raise_for_status()
        players = response.json()

        # Filter out the previously selected player
        available_players = [player for player in players if player['id'] != previous_selected_player_id]

        # Select a random player from the available players
        selected_player = choice(available_players)

        # Update the SelectedPlayer instance in the local database
        selected_player_instance, _ = SelectedPlayer.objects.get_or_create(date=today)
        selected_player_instance.player_id = selected_player['id']
        selected_player_instance.save()

        self.stdout.write(self.style.SUCCESS('Selected player updated successfully for today'))
