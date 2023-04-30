from django.contrib import admin
from .models import Team, League, Game


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'goals', 'scores')


@admin.register(League)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_side', 'opposite_side', 'first_side_goals', 'opposite_side_goals', 'created_date')