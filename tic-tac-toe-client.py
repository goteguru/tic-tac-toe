import requests

#jatek allas lekerdezese
def jatek_lekerdezes():
    r = requests.get('http://192.168.111.183/game')
    print('- - - - - - -')
    print('|', r[0], '|', r[1], '|', r[2], '|')
    print('- - - - - - -')
    print('|', r[3], '|', r[4], '|', r[5], '|')
    print('- - - - - - -')
    print('|', r[6], '|', r[7], '|', r[8], '|')
    print('- - - - - - -')


#pozicio kuldese
def pozicio_kuldese():
    pozicio = input("Hova lepsz? ")
    if 'x' in pozicio:
        print(requests.post('http://192.168.111.183/x', data = {'pos':pozicio}))
    else:
        print(requests.post('http://192.168.111.183/o', data = {'pos':pozicio}))
