# tic-tac-toe
tictacto kliens szerver gyakorlat.

REST API dokumentáció
--------------------

### Új játék létrehozása: POST /game/new
 
* **Response**: 

    * OK (200): 
    ```
    id=[int]: új játék azonosítója
    game=[string]: játéktábla (általában üres tábla)
    ```


### Futó és befejezett játékok listája: GET /games

* **Response**: 

  * OK (200): futó játékok listája
   ```javascript
   {
   <game_id>: {game:"____XO___", result:"X"},
   <game_id>: {...}, 
   <game_id>: {...}
   }
   ```
 

### Játéktábla lekérdezése: GET /game/{id}

* **URL params**: {id}=[int] kért játék azonosítója
* **Response**: 

  * OK (200): 
  ```
  game=[string]: játék táblája. Pl: "\_\_\_XO\_\_X\_\_"
  result=[char]: játék eredménye. Lehetséges értékek: 'O'|'X'|'-'|''
  
  döntetlen esetén '-', folyamatban lévő játék esetén:''
  ```    
  * NOT_FOUND (404): a játéktábla {id} nem található, content: hibaüzenet.

### Lépés: PUT /game/{id}/{p}/{pos}  
* **URL Params**: 
  ```
  {id}=[int]: Game id
  {p}='X'|'O': Játékos, helyes érték 'X' vagy 'O'.
  {pos}=[int]: Választott pozíció. Lehetséges értékei: 1-9
  ```
* **Response**:
  
  * OK (200): lépés sikeres. content: ```{game:"___XO____", result:""}```
  * NOT_FOUND (404): pozíció nem található. content: hibaüzenet.
  * FORBIDDEN (403): szabálytalan lépés. content: hibaüzenet.
  * BAD_REQUEST (400): hibás adat. content: hibaüzenet.

### Játék törlése: DELETE  /game/{id}
* **URL Params**: 
``` 
  {id}=[int]: Game id
```
  
* **Response**:
  
  * OK (200): Törlés sikeres. Content: none
  * NOT_FOUND (404): Játék nem található. content: hibaüzenet.
  




