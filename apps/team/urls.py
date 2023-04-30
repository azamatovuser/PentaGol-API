from django.urls import path
from .views import TeamListAPIView, TeamsPlayingNextWeek, TeamsPlayedLastWeek


urlpatterns = [
    path('top_teams/', TeamListAPIView.as_view()),
    path('teams_playing_next_week/', TeamsPlayingNextWeek.as_view()),
    path('teams_played_last_week/', TeamsPlayedLastWeek.as_view()),
]