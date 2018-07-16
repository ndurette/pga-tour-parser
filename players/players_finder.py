import requests
from players.player import Player

__players_list__ = []


def find_player(player_id, name):
    for p in __list_players__():
        if p.player_id == player_id:
            return p
        if p.full_name == name:
            return p


def __list_players__():
    if not __players_list__:
        data = __request_players__()
        for p in data['plrs']:
            if p['pid'] and p['nameF'] and p['nameL']:
                __players_list__.append(Player(int(p['pid']), p['nameF'], p['nameL']))

    return __players_list__


def __request_players__():
    r = requests.get("https://statdata.pgatour.com/players/player.json")
    if r.status_code == requests.codes.ok:
        return r.json()
