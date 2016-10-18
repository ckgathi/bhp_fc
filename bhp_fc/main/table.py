

class Table(object):

    def __init__(self, teams):

        self.teams = None  # A list of teams in the league
        self.order_table_list = []

    def goal_difference(self, team):
        pass

    def goal_forward(self, team):
        pass

    def goal_agaist(self, team):
        pass

    def points(self, team):
        pass

    def games_drew(self, team):
        pass

    def games_lost(self, team):
        pass

    def games_won(self, team):
        pass

    def games_played(self, team):
        pass

    @property
    def order_table_list(self):
        table_team_list = []
        for team in self.teams:
            pass   # Order teams by top team in the league, consider goal difference and other issues
        return table_team_list
