from django.contrib import admin
from django.urls import path
from app.player.views.player import PlayerListCreateAPIView, PlayerRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/', PlayerListCreateAPIView.as_view(), name='player-list-create'),
    path('players/<int:pk>/', PlayerRetrieveUpdateDestroyAPIView.as_view(), name='player-retrieve-update-destroy'),
]
