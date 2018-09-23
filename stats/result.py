import argparse
import json

import os

from stats import scoring_rule
from players import players_finder
from stats.pooler import Pooler
from tournaments.tournament import Tournament


def parse_players():
    with open("../data/players.json") as f:
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
    with open("../data/tournaments.json") as f:
        data = json.load(f)

    tournaments = {}
    for t in data:
        try:
            tournament = Tournament(t['id'], t['name'], t['year'], scoring_rule.rule(t['type']))
            if not t.get('skipAdjust', None):
                scoring_rule.adjust_scoring(tournament)
            tournaments[t['id']] = tournament
        except:
            print("unable to get info for: " + t['name'])

    return tournaments


def parse_poolers():

    poolers = []
    for filename in os.listdir("../data/pooler/"):

        with open("../data/pooler/" + filename) as f:
            data = json.load(f)
            poolers.append(Pooler(data['name'], data['seasons']))

    return poolers


def compute_point(tournament, player_id):
    for entry in tournament.leaderboard.leader_board:
        if player_id == entry.player_id:
            if not entry.position:
                continue
            elif entry.position[0] == 'T':
                return tournament.points.get(entry.position[1:], 0)
            else:
                return tournament.points.get(entry.position, 0)

    return 0


def score_poolers(poolers, tournaments):
    print("\n\n============== POOLER ==============")
    for pooler in poolers:
        pooler_score = 0

        for s in pooler.seasons:
            for p in s['players']:
                for t in s['tournaments']:
                    pooler_score += compute_point(tournaments[t], p)

        print(pooler.name + ": " + "{:10.2f}".format(pooler_score))


def score_players(players, tournaments):
    print("\n\n============== PLAYERS ==============")
    for p in players:
        score = 0
        for t in tournaments:
            score += compute_point(tournaments[t], players[p].player_id)

        print(players[p].name() + ": " + "{:10.2f}".format(score))


if __name__ == '__main__':
    tournaments = parse_tournaments()
    players = parse_players()
    poolers = parse_poolers()

    score_poolers(poolers, tournaments)
    score_players(players, tournaments)
