from django.db import models
from django.utils import timezone
from app.player.models.player import Player

class SelectedPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.name} - {self.date}"
    
    class Meta:
        db_table = 'selected_player'
        verbose_name = 'Selected Player'
        verbose_name_plural = 'Selected Players'
        ordering = ['-date']
        app_label = 'player'