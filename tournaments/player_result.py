import requests


def get_result(player_id, year):
    return request_results(player_id, year)


def request_results(player_id, year):
    r = requests.get("https://statdata.pgatour.com/players/" + str(player_id) + "/" + str(year) + "results.json")
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        print(r.json())
        return r.json()


if __name__ == '__main__':
    print(get_result(28089, 2018))
