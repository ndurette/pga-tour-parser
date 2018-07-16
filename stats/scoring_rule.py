import json


def rule(type):
    if type == "small":
        return SmallRule()
    elif type == "medium":
        return MediumRule()
    elif type == "major":
        return MajorRule()
    elif type == "zurich":
        return ZurichRule()
    elif type == "dell":
        return DellRule()


def adjust_scoring(tournament):
    divider = 0
    accumulated_points = 0
    start_index = None
    for entry in tournament.leaderboard.leader_board:

        if entry.position == 'CUT' or len(entry.position) < 1:
            continue
        elif entry.position[0] == 'T':
            if start_index and start_index != entry.position[1:]:
                for i in range(divider):
                    tournament.points[str(int(start_index) + i)] = accumulated_points / divider

                divider = 0
                accumulated_points = 0
                start_index = None

            else:
                start_index = entry.position[1:]

            accumulated_points += tournament.scoring_rule.points.get(str(int(entry.position[1:]) + divider), 0)
            divider += 1
        else:
            for i in range(divider):
                tournament.points[str(int(start_index) + i)] = accumulated_points / divider

            divider = 0
            accumulated_points = 0
            start_index = None
            tournament.points[entry.position] = tournament.scoring_rule.points.get(entry.position, 0)


class ScoringRule:

    def __init__(self, type):
        self.type = type
        self.points = None


class SmallRule(ScoringRule):

    def __init__(self):
        super().__init__(1)
        with open('rules/small.json') as f:
            self.points = json.load(f)


class MediumRule(ScoringRule):

    def __init__(self):
        super().__init__(1)
        with open('rules/medium.json') as f:
            self.points = json.load(f)


class MajorRule(ScoringRule):

    def __init__(self):
        super().__init__(1)
        with open('rules/major.json') as f:
            self.points = json.load(f)


class ZurichRule(ScoringRule):

    def __init__(self):
        super().__init__(1)
        with open('rules/zurich.json') as f:
            self.points = json.load(f)


class DellRule(ScoringRule):

    def __init__(self):
        super().__init__(1)
        with open('rules/dell.json') as f:
            self.points = json.load(f)
