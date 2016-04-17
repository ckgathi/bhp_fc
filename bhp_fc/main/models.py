from django.db import models


class Fixture(models.Model):
    bhp_team = models.CharField(max_length=200)
    team_agaist = models.CharField(max_length=200)
    game_datetime = models.DateTimeField('date published')
    grounds = models.CharField(max_length=200)

    def __str__(self):
        return (self.bhp_team, self.team_agaist)


class Result(models.Model):
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    bhp_score = models.IntegerField(default=0)
    team_agaist_score = models.IntegerField(default=0)

    def __str__(self):
        return self.fixture
