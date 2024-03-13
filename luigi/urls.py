from django.contrib import admin
from django.urls import path
from app.player.views.player import PlayerListCreateAPIView, PlayerRetrieveUpdateDestroyAPIView
from app.player.views.selected_player import SelectedPlayerRetrieveUpdateDestroyAPIView, FetchSelectedPlayerAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/', PlayerListCreateAPIView.as_view(), name='player-list-create'),
    path('players/<int:pk>/', PlayerRetrieveUpdateDestroyAPIView.as_view(), name='player-retrieve-update-destroy'),
    path('selected-players/', FetchSelectedPlayerAPIView.as_view(), name='selected-player-list-create'),
    path('selected-players/<int:pk>/', SelectedPlayerRetrieveUpdateDestroyAPIView.as_view(), name='selected-player-retrieve-update-destroy'),
]
