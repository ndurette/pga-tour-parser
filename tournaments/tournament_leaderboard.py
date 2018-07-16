import requests


class TournamentLeaderBoard:

    def __init__(self, tournament_id, year):
        self.tournament_id = tournament_id
        self.year = year
        self.leader_board = self.__get_leader_board__()

    def __get_leader_board__(self):
        players = []
        if self.tournament_id == "470":
            for r in self.__request_leader_board__()['rounds']:
                for b in r['brackets']:
                    for g in b['groups']:
                        for p in g['players']:
                            if p['curPos']:
                                players.append(LeaderBoardEntry(p['curPos'], p['pid']))

        else:
            for p in self.__request_leader_board__()['leaderboard']['players']:
                players.append(LeaderBoardEntry(p['current_position'], p['player_id']))
        return players

    def __request_leader_board__(self):
        if self.tournament_id == "470":
            r = requests.get("https://statdata.pgatour.com/r/" + self.tournament_id + "/" + self.year + "/leaderboard_mp.json")
        else:
            r = requests.get("https://statdata.pgatour.com/r/" + self.tournament_id + "/" + self.year + "/leaderboard-v2.json")
        if r.status_code == requests.codes.ok:
            return r.json()


class LeaderBoardEntry:

    def __init__(self, position, player_id):
        self.position = position
        self.player_id = int(player_id)

    def __str__(self):
        return self.position + ": " + str(self.player_id)

    def __repr__(self):
        return str(self)
