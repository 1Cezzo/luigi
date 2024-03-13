from django.core.management.base import BaseCommand
from random import choice
from app.player.models import Player, SelectedPlayer
from datetime import datetime, timezone

class Command(BaseCommand):
    help = 'Selects a new player for the current day'

    def handle(self, *args, **options):
        today = datetime.now(timezone.utc).date()

        try:
            previous_selected_player_instance = SelectedPlayer.objects.get(date=today)
            previous_selected_player = previous_selected_player_instance.player
        except SelectedPlayer.DoesNotExist:
            previous_selected_player = None

        available_players = Player.objects.exclude(id=previous_selected_player.id) if previous_selected_player else Player.objects.all()

        selected_player = choice(available_players)
        selected_player_instance, _ = SelectedPlayer.objects.get_or_create(date=today)
        selected_player_instance.player = selected_player
        selected_player_instance.save()

        self.stdout.write(self.style.SUCCESS('Selected player updated successfully for today'))
