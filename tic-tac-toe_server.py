from bottle import get, post, run, request, response
import json
game="_________"
endgame=[(0,1,2), (3,4,5), (6,7,8), (0,4,8), (2,4,6)]

def lep(ember):
    response.content_type = 'application/json'
    pos=request.form.get-1
    if game[pos]=="-":
        game[pos]=ember
        for i in endgame:
            if i[0]==i[1]==i[2]:
                return json.dumps({"error": 0, "result": ember})
        return json.dumps({"error": 0, "game": game})
    else:
        for i in endgame:
            if i[0]==i[1]==i[2]:
                 return json.dumps({"error": 0, "result": "_"})   
        return json.dumps({"error": 1, "message": "foglalt"})
        
    
@post("/x")
def x():
    lep("x")

@post("/o")
def o():
    lep("o")


@get("/game")
def return_game():
    json.dumps({"error": 0, "game": game})
   
run(host='192.168.111.183', port=1111, debug=True)
