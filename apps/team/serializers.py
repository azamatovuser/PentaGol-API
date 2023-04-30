from rest_framework import serializers
from .models import Game, League, Team


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'title']


class TeamSerializer(serializers.ModelSerializer):
    league = LeagueSerializer(read_only=True)
    class Meta:
        model = Team
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'first_side', 'opposite_side', 'first_side_goals', 'opposite_side_goals', 'created_date']