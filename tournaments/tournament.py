class Tournament:
    def __init__(self, tournament_id, tournament_name):
        self.tournament_id = tournament_id
        self.tournament_name = tournament_name

    def __repr__(self):
        return "{ " + self.tournament_id + ": " + self.tournament_name + " }"

    def __str__(self):
        return "{ " + self.tournament_id + ": " + self.tournament_name + " }"
