class Player:

    def __init__(self, player_id, first_name, last_name):
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{ " + str(self.player_id) + ": " + self.full_name + " }"
