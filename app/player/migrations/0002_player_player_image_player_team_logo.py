# Generated by Django 5.0.2 on 2024-03-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='player_image',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='team_logo',
            field=models.URLField(blank=True),
        ),
    ]
