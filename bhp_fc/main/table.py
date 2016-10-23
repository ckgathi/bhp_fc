from django.db.models import Q

from bhp_fc.main.models import Fixture, Result


class Table(object):

    def __init__(self):

        self.teams = None  # A list of teams in the league

    def goal_difference(self, team):
        return self.goal_forward(team) - self.goal_agaist(team)

    def goal_forward(self, team):
        team_results = self.team_results(team)
        team_goals = 0
        for team_result in team_results:
            if team_result.fixture.team_home == team:
                team_goals += team_result.team_home_score
            elif team_result.fixture.team_away == team:
                team_goals += team_result.team_agaist_score
        return team_goals

    def goal_agaist(self, team):
        team_results = self.team_results(team)
        team_goals_agaist = 0
        for team_result in team_results:
            if team_result.fixture.team_home == team:
                team_goals_agaist += team_result.team_agaist_score
            elif team_result.fixture.team_away == team:
                team_goals_agaist += team_result.team_home_score
        return team_goals_agaist

    def points(self, team):
        draw_points = self.games_drew(team)
        win_points = self.games_won(team) * 3
        return draw_points + win_points

    def games_drew(self, team):
        team_results = self.team_results(team)
        draw = 0
        for team_result in team_results:
            if team_result.fixture.team_home == team:
                if team_result.team_home_score == team_result.team_agaist_score:
                    draw += 1
            elif team_result.fixture.team_away == team:
                if team_result.team_agaist_score == team_result.team_home_score:
                    draw += 1
        return draw

    def games_lost(self, team):
        team_results = self.team_results(team)
        loss = 0
        for team_result in team_results:
            if team_result.fixture.team_home == team:
                if team_result.team_home_score < team_result.team_agaist_score:
                    loss += 1
            elif team_result.fixture.team_away == team:
                if team_result.team_agaist_score < team_result.team_home_score:
                    loss += 1
        return loss

    def games_won(self, team):
        team_results = self.team_results(team)
        win = 0
        for team_result in team_results:
            if team_result.fixture.team_home == team:
                if team_result.team_home_score > team_result.team_agaist_score:
                    win += 1
            elif team_result.fixture.team_away == team:
                if team_result.team_agaist_score > team_result.team_home_score:
                    win += 1
        return win

    def games_played(self, team):
        return self.team_results(team).count()


#     def order_table_list(self):
#         table_team_list = []
#         for team in self.teams:
#             pass   # Order teams by top team in the league, consider goal difference and other issues
#         return table_team_list

    def team_fixtures(self, team_name):
        team_fixtures = Fixture.objects.filter(Q(team_home=team_name, fixture_type='league') | Q(team_away=team_name, fixture_type='league'))
        return team_fixtures

    def team_results(self, team_name):
        results = Result.objects.filter(Q(fixture__team_home=team_name, fixture__fixture_type='league') | Q(fixture__team_away=team_name, fixture__fixture_type='league'))
        return results
