from bottle import get, post, run, request, response, static_file
import json
game=list("_________")
endgame=[(0,1,2), (3,4,5), (6,7,8), (0,4,8), (2,4,6)]

def lep(ember):
    if game.count("x")==game.count("o"):
        turn="x"
    else:
        turn="o"
    global game
    response.content_type = 'application/json'
    pos=int(request.forms.get("pos"))-1
    if pos not in [0,1,2,3,4,5,6,7,8]:
        return json.dumps({"error": 1, "message": "outofrange"})
    if turn==ember:
        if game[pos]=="_":
            game[pos]=ember
            print (game)
            for i in endgame:
                if i[0]==i[1]==i[2]==ember:
                    return json.dumps({"error": 0, "result": ember})
                if "_" not in game:
                    return json.dumps({"error": 0, "result": "_", "game": "".join(game)})  
            return json.dumps({"error": 0, "game": "".join(game)})
        else:
            return json.dumps({"error": 1, "message": "foglalt"})
    else:
        return json.dumps({"error": 1, "message": "notturn"})
        
    
@post("/x")
def x():
    lep("x")

@post("/o")
def o():
    lep("o")

@get("/newgame")
def newgame():
    global game
    game=list("________")
    return json.dumps({"error": 0, "game": "".join(game)})

@get("/game")
def return_game():
    return json.dumps({"error": 0, "game": "".join(game)})

@get('/client')
def client():
    return static_file("tic-tac-toe_client.html", ".")

run(host='', port=1111, debug=True)
