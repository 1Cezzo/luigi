from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    team_name = models.CharField(max_length=100)
    team_logo = models.URLField(max_length=200, blank=True)
    player_image = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'player'
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        ordering = ['name']
        app_label = 'player'
