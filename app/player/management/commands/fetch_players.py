import requests
from app.player.models.player import Player
from django.core.management.base import BaseCommand
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Fetches and saves player data from an external API'

    def handle(self, *args, **options):
        logger.info("Fetching player data...")

        url = "https://api-football-v1.p.rapidapi.com/v3/players"

        headers = {
            "X-RapidAPI-Key": os.getenv('API_KEY'),
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        try:
            for page_num in range(0, 49):
                querystring = {"league": "39", "season": "2023", "page": str(page_num)}
                response = requests.get(url, headers=headers, params=querystring)

                if response.status_code == 200:
                    data = response.json()
                    players = data.get("response", [])

                    for player_data in players:
                        player = player_data.get("player")
                        if player:
                            appearances = player_data["statistics"][0]["games"].get('appearences', 0)
                            if appearances is not None and appearances >= 5:
                                first_name = player.get("firstname", "").split()[0]
                                last_name = player.get("lastname", "")
                                player_name = f"{first_name} {last_name}".strip()
                                player_age = player.get("age")
                                player_nationality = player.get('nationality', "Unknown")
                                if player_data.get('statistics'):
                                    if player_data['statistics'][0].get('team'):
                                        team_name = player_data['statistics'][0]['team'].get('name', "Unknown")
                                    else:
                                        team_name = "Unknown"
                                else:
                                    team_name = "Unknown"
                                if player.get('photo'):
                                    player_image = player.get('photo')
                                if player_data['statistics'][0].get('team').get('logo'):
                                    team_logo = player_data['statistics'][0]['team'].get('logo')

                                if player_name and player_age and player_nationality and team_name:
                                    Player.objects.update_or_create(
                                        name=player_name,
                                        defaults={
                                            'age': player_age,
                                            'nationality': player_nationality,
                                            'team_name': team_name,
                                            'player_image': player_image,
                                            'team_logo': team_logo
                                        }
                                    )

                    logger.info(f"Page {page_num} data fetched and saved successfully.")
                else:
                    logger.warning(f"Error fetching player data for page {page_num}: {response.status_code}")
        except requests.RequestException as e:
            logger.error(f"Error fetching player data: {e}")
