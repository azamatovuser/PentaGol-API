from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='team_image/')
    goals = models.IntegerField()
    o = models.IntegerField()

    def __str__(self):
        return self.name