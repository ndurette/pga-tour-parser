import requests
from players import player


def list_players():
    data = request_players()
    players = []
    for p in data['plrs']:
        if p['pid'] and p['nameF'] and p['nameL']:
            players.append(player.Player(p['pid'], p['nameF'], p['nameL']))

    return players


def request_players():
    r = requests.get("https://statdata.pgatour.com/players/player.json")
    if r.status_code == requests.codes.ok:
        return r.json()


if __name__ == '__main__':
    print(list_players())
