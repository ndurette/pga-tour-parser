import requests
from players import player


def list_players():
    data = request_players()
    players = []
    for p in data['plrs']:
        if p['pid'] and p['nameF'] and p['nameL']:
            players.append(player.Player(int(p['pid']), p['nameF'], p['nameL']))

    return players


def find_player(player_id, name):
    for p in list_players():
        if p.player_id == player_id:
            return p
        if p.full_name == name:
            return p


def request_players():
    r = requests.get("https://statdata.pgatour.com/players/player.json")
    if r.status_code == requests.codes.ok:
        return r.json()


if __name__ == '__main__':
    print(list_players())
    print(find_player(28089, None))
    print(find_player(None, "Jason Day"))
