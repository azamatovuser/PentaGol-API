from rest_framework import generics
from .serializers import TeamSerializer, GameSerializer, LeagueSerializer
from .models import Team, Game, League


class TeamListAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer