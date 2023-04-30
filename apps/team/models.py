from django.db import models


class League(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='team_image/')
    played_games = models.IntegerField()
    goals = models.IntegerField()
    scores = models.IntegerField()
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Game(models.Model):
    first_side = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='first_side')
    opposite_side = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='opposite_side')
    first_side_goals = models.IntegerField()
    opposite_side_goals = models.IntegerField()
    created_date = models.DateTimeField()