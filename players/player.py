class Player:

    def __init__(self, player_id, first_name, last_name):
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.number_of_scoring = dict({})
        self.score = 0

    def __repr__(self):
        return str(self)

    def __str__(self):
        d = dict({})
        d['player_id'] = self.player_id
        d['full_name'] = self.full_name
        d['score'] = self.score
        d['number_of_scoring'] = str(self.number_of_scoring)
        return str(d)

    def add_point(self, point, tournament):
        if point > 0:
            self.number_of_scoring[tournament.tournament_id] = point
            self.score += point
