from bottle import get, post, run, request, response, put, delete
import json
id=0
games={}
endgame=[(0,1,2), (3,4,5), (6,7,8), (0,4,8), (2,4,6)]

@put("/game/<id>/<p>/<pos>")
def lep(id, ember, pos):
    if game.count("x")==games[id][0].count("o"):
        turn="x"
    else:
        turn="o"
    global games
    response.content_type = 'application/json'
    pos+=-1
    if pos not in range(games[id][1][0]*games[id][1][1]):
        response.content_type = 'application/text'
        response.status=404
        return "hibás pozíció"
    if turn==ember:
        if games[id][0][pos]=="_":
            a=list(games[id][0])
            a[pos]=ember
            games[id][0]="".join(a)
            print (game)
            for i in endgame:
                if i[0]==i[1]==i[2]==ember:
                    return json.dumps({"error": 0, "result": ember})
                if "_" not in game:
                    return json.dumps({"error": 0, "result": "_", "game": "".join(game)})  
            return json.dumps({"error": 0, "game": "".join(game)})
        else:
            response.content_type = 'application/text'
            response.status=403
            return "foglalt"
    else:
        response.content_type = 'application/text'
        response.status=403
        return "nem te köröd"

@post("/game/new/<width:int>x<height:int>")
def newgame(width, height):
    global games, id
    id+=1
    if 100<width<3 or 100<width<3 :
        response.content_type = 'application/text'
        response.status=400
        return "hibás adat"
    games.update({id:[(width*height)*"_", (width, height), request.form.get("win_length")]})
    return json.dumps({"error": 0, "games": games})

@get("/games")
def return_game():
    return json.dumps({"error": 0, "game": games})

@get("/game/<id>")
def return_game(id):
    if id not in games.keys:
        response.content_type = 'application/text'
        response.status=404
        return "játék nem található"
    return json.dumps({"error": 0, "game": games[id][0], "result": ""})

@delete(/game/<id>)
def delete(id):
    if id not in games.keys:
        response.content_type = 'application/text'
        response.status=404
        return "játék nem található"
    games.pop(id)

run(host='192.168.111.105', port=1111, debug=True)
