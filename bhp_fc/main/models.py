from django.db import models


class Fixture(models.Model):

    team_a = models.CharField(max_length=200, verbose_name="Name of team home",)

    team_agaist = models.CharField(max_length=200, verbose_name="Name of team away",)

    game_datetime = models.DateTimeField(
        verbose_name="Kick off time",
        blank=True,
        null=True,)

    grounds = models.CharField(
        verbose_name="Grounds where the game is played.",
        blank=True,
        null=True,
        max_length=200)

    def __str__(self):
        return '{0} vs {1}'.format(self.bhp_team, self.team_agaist)

    class Meta:
        app_label = 'main'
        verbose_name = "Fixture"
        verbose_name_plural = "Fixture"


class Result(models.Model):
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    team_home_score = models.IntegerField(
        verbose_name="Team home Scored goals.",
        blank=True,
        null=True,
        default=0)
    team_agaist_score = models.IntegerField(
        verbose_name="Team away Scored goals.",
        blank=True,
        null=True,
        default=0)

    def __str__(self):
        return '{0} {1} -- {2} {3}'.format(self.fixture.bhp_team, self.bhp_score, self.team_agaist_score, self.fixture.team_agaist)

    class Meta:
        app_label = 'main'
        verbose_name = "Result"
        verbose_name_plural = "Result"


class Team(models.Model):
    name = models.CharField(max_length=200)

    team_grounds = models.CharField(max_length=200)

    games_played = models.IntegerField(
        verbose_name="Opponent Scored goals.",
        blank=True,
        null=True,
        default=0)

    games_won = models.IntegerField(
        verbose_name="Opponent Scored goals.",
        blank=True,
        null=True,
        default=0)

    games_drew = models.IntegerField(
        verbose_name="Opponent Scored goals.",
        blank=True,
        null=True,
        default=0)

    games_lost = models.IntegerField(
        verbose_name="Opponent Scored goals.",
        blank=True,
        null=True,
        default=0)

    goal_forward = models.IntegerField(
        verbose_name="Opponent Scored goals.",
        blank=True,
        null=True,
        default=0)

    goal_agaist = models.IntegerField(
        verbose_name="Opponent Scored goals.",
        blank=True,
        null=True,
        default=0)

    goal_difference = models.IntegerField(
        verbose_name="Opponent Scored goals.",
        blank=True,
        null=True,
        default=0)

    points = models.IntegerField(
        verbose_name="Opponent Scored goals.",
        blank=True,
        null=True,
        default=0)

    def __str__(self):
        return '{0}'.format(self.name)

    class Meta:
        app_label = 'main'
        verbose_name = "Team"
        verbose_name_plural = "Team"


class SlideShow(models.Model):

    image_name = models.CharField(max_length=200, verbose_name="Name of the picture",)

    image_title = models.CharField(max_length=200, verbose_name="Title of the picture",)

    pic_discription = models.TextField(
        verbose_name="Description of the picture",
        max_length=250,
        blank=True,
        null=True)

    def __str__(self):
        return self.image_title

    class Meta:
        app_label = 'main'
        verbose_name = "SlideShow"
        verbose_name_plural = "Slide Show"
