import requests


class PlayerResult:

    def __init__(self, tournament_id, position):
        self.tournament_id = tournament_id
        self.position = position

    def __str__(self):
        d = dict({})
        d['tournament_id'] = self.tournament_id
        d['position'] = self.position
        return str(d)

    def __repr__(self):
        return str(self)


def get_result(player_id, year):
    results = []
    for r in request_results(player_id, year)['plrs'][0]['tours'][0]['trnDetails']:
        results.append(PlayerResult(r['trn']['permNum'], r['finPos']['value']))
    return results


def request_results(player_id, year):
    r = requests.get("https://statdata.pgatour.com/players/" + str(player_id) + "/" + year + "results.json")
    if r.status_code == requests.codes.ok:
        return r.json()


if __name__ == '__main__':
    print(get_result(28089, str(2018)))
