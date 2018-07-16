import json
from stats import tournament_stats, scoring_rule
from players import players_finder
from tournaments.tournament import Tournament


def parse_players():
    with open("../pool/players.json") as f:
        data = json.load(f)

    players = dict({})
    for p in data:
        player = players_finder.find_player(p['player_id'], p['full_name'])
        if player:
            players[player.player_id] = player
        else:
            print("unable to find :\n" + str(p))
    return players


def parse_tournaments():
    with open("../pool/2018-1/tournaments.json") as f:
        data = json.load(f)

    tournaments = []
    for t in data:
        try:
            tournament = Tournament(t['id'], t['name'], str(2018), scoring_rule.rule(t['type']))
            if not t.get('skipAdjust', None):
                scoring_rule.adjust_scoring(tournament)
            tournaments.append(tournament)
        except:
            print("unable to get info for: " + t['name'])

    return tournaments


def score_poolers(players):
    with open("../pool/2018-1/pool.json") as f:
        data = json.load(f)

    for pooler in data:
        pooler_score = 0

        for p_id in pooler['players']:
            p = players.get(p_id)
            pooler_score += p.score

        print(pooler['name'] + ": " + "{:10.2f}".format(pooler_score))


if __name__ == '__main__':
    tournaments = parse_tournaments()
    players = parse_players()
    for p in players.values():
        tournament_stats.compute_points(tournaments, p)
        print(p)

    score_poolers(players)
