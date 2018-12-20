import requests

#jatek allas lekerdezese
def jatek_lekerdezes():
    response = requests.get('http://192.168.111.105:1111/game')
    r = response.json()["game"]
    print('- - - - - - -')
    print('|', r[0], '|', r[1], '|', r[2], '|')
    print('- - - - - - -')
    print('|', r[3], '|', r[4], '|', r[5], '|')
    print('- - - - - - -')
    print('|', r[6], '|', r[7], '|', r[8], '|')
    print('- - - - - - -')

#pozicio kuldese
def pozicio_kuldese(jatekos):
    pozicio = input("Hova lepsz? ")
    if 'x' in jatekos:
        print(requests.post('http://192.168.111.105:1111/x', data = {'pos':pozicio}))
        print(requests.request())
    else:
        print(requests.post('http://192.168.111.105:1111/o', data = {'pos':pozicio}))

def uj_jatek(width, height, win_length):
    data = {'win_length': win_length}
    print(requests.post('http://192.168.111.105:1111/game/new/' + str(width) + 'x' + str(height), data = data))
    response = requests.get('http://192.168.111.105:1111/game')

    if response.status_code == 200:
        return jatek_lekerdezes()
    elif response.status_code == 404:
        return 'pozíció nem található'
    elif response.status_code == 403:
        return 'szabalytalan lepes'
    elif response.status_code == 400:
        return 'hibas adat'
    else:
        resp = response.json()
        print(resp)
        print(resp["game"])
        print(resp["id"])


def lepes(id, p, pos):
    print(requests.post('http://192.168.111.105:1111/game/' + id + p + pos))


