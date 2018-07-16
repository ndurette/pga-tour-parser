from tournaments import tournament_leaderboard


class Tournament:
    def __init__(self, tournament_id, tournament_name, year, rule):
        self.tournament_id = tournament_id
        self.tournament_name = tournament_name
        self.year = year
        self.leaderboard = tournament_leaderboard.TournamentLeaderBoard(tournament_id, year)
        self.scoring_rule = rule
        self.points = rule.points

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{ " + self.tournament_id + ": " + self.tournament_name + " }"
