from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length = 100)
    logo = models.ImageField(upload_to='team_logos/')
    conference = models.CharField(max_length = 5)
    division = models.CharField(max_length = 100)
    nba_titles = models.IntegerField()

    def __str__(self):
        return f'{self.name} / {self.conference}'


class Player(models.Model):
    name = models.CharField(max_length = 100)
    photo = models.ImageField(upload_to='player_face/')
    shirt_number = models.IntegerField()
    age = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'