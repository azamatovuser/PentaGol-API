from rest_framework import generics
from .serializers import TeamSerializer, GameSerializer, LeagueSerializer
from .models import Team, Game, League
from datetime import datetime, timedelta
from django.db.models import Q


class TeamListAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamsPlayingNextWeek(generics.ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        today = datetime.now().date()
        start_date = today + timedelta(days=7-today.weekday())
        end_date = start_date + timedelta(days=7)
        next_week_games = Game.objects.filter(created_date__range=(start_date, end_date))
        team_ids = set()
        for game in next_week_games:
            team_ids.add(game.first_side_id)
            team_ids.add(game.opposite_side_id)
        category = self.request.query_params.get('category', None)
        if category:
            return Team.objects.filter(pk__in=team_ids, league__title=category)
        else:
            return Team.objects.filter(pk__in=team_ids)


class TeamsPlayingLastWeek(generics.ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        today = datetime.now().date()
        start_date = today + timedelta(days=7-today.weekday())
        end_date = start_date + timedelta(days=7)
        next_week_games = Game.objects.filter(created_date__range=(start_date, end_date))
        team_ids = set()
        for game in next_week_games:
            team_ids.add(game.first_side_id)
            team_ids.add(game.opposite_side_id)
        category = self.request.query_params.get('category', None)
        if category:
            return Team.objects.filter(pk__in=team_ids, league__title=category)
        else:
            return Team.objects.filter(pk__in=team_ids)


class TeamsPlayedLastWeek(generics.ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        today = datetime.now().date()
        start_date = today - timedelta(days=today.weekday()+7)
        end_date = today

        # Filter for games that were played during last week
        last_week_games = Game.objects.filter(created_date__range=(start_date, end_date))

        # Get the teams that played last week
        team_ids = set()
        for game in last_week_games:
            team_ids.add(game.first_side_id)
            team_ids.add(game.opposite_side_id)

        # Query for the teams
        return Team.objects.filter(pk__in=team_ids)