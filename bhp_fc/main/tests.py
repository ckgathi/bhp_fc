from datetime import timedelta

from django.utils import timezone
from django.test import TestCase

from .table import Table
from .models import Fixture, Result


class TestTable(TestCase):

    def setUp(self):
        self.fixture1 = Fixture.objects.create(team_home='bhp_fc', team_away='gss_fc', game_datetime=timezone.now() + timedelta(days=-1), grounds='gss_grounds')
        self.fixture2 = Fixture.objects.create(team_home='bhp_fc', team_away='gss_fc', game_datetime=timezone.now() + timedelta(days=-2), grounds='gss_grounds')
        self.fixture3 = Fixture.objects.create(team_home='gss_fc', team_away='bhp_fc', game_datetime=timezone.now() + timedelta(days=-3), grounds='gss_grounds')
        self.fixture4 = Fixture.objects.create(team_home='bhp_fc', team_away='gss_fc', game_datetime=timezone.now() + timedelta(days=-4), grounds='gss_grounds')
        self.fixture5 = Fixture.objects.create(team_home='moh_fc', team_away='bhp_fc', game_datetime=timezone.now() + timedelta(days=-5), grounds='notwane_grounds')
        self.fixture6 = Fixture.objects.create(team_home='motopi_fc', team_away='bhp_fc', game_datetime=timezone.now(), grounds='notwane_grounds')
        self.result1 = Result.objects.create(fixture=self.fixture1, team_home_score=1, team_agaist_score=1)
        self.result2 = Result.objects.create(fixture=self.fixture2, team_home_score=1, team_agaist_score=2)
        self.result3 = Result.objects.create(fixture=self.fixture3, team_home_score=2, team_agaist_score=5)
        self.result4 = Result.objects.create(fixture=self.fixture4, team_home_score=5, team_agaist_score=0)
        self.result5 = Result.objects.create(fixture=self.fixture5, team_home_score=3, team_agaist_score=2)
        self.team_name = 'bhp_fc'

    def test_games_won(self):
        games_won = Table().games_won(self.team_name)
        self.assertEqual(games_won, 2)

    def test_games_lost(self):
        games_lost = Table().games_lost(self.team_name)
        self.assertEqual(games_lost, 2)

    def test_games_drew(self):
        games_drew = Table().games_drew(self.team_name)
        self.assertEqual(games_drew, 1)

    def test_points(self):
        points = Table().points(self.team_name)
        self.assertEqual(points, 7)

    def test_goal_difference(self):
        goal_diff = Table().goal_difference(self.team_name)
        self.assertEqual(goal_diff, 6)

    def test_goal_forward(self):
        goal_forward = Table().goal_forward(self.team_name)
        self.assertEqual(goal_forward, 14)

    def test_goal_agaist(self):
        goal_agaist = Table().goal_agaist(self.team_name)
        self.assertEqual(goal_agaist, 8)

    def test_games_played(self):
        games_played = Table().games_played(self.team_name)
        self.assertEqual(games_played, 5)

    def test_team_fixtures(self):
        team_fixtures = Table().team_fixtures(self.team_name)
        self.assertEqual(team_fixtures.count(), 6)

    def test_team_results(self):
        team_results = Table().team_results(self.team_name)
        self.assertEqual(team_results.count(), 5)
