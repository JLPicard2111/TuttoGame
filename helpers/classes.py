class Dice:
    instances = []
    def __init__(self, id, value, valid, keep, triple):
        """Erstellt ein Würfel Objekt. Folgende Dinge müssen angegeben werden:
            - Aktueller Wert des Würfels
            - Boolean, ob er gehalten wird oder weiter gewürfelt wird
            - Nummer des Würfels (1 bis 6)
            - Ob der Würfel einen gültigen Wert enthielt
            - Ob der Wert des Würfels im Wurf 3x vorkam"""
        self.value = value
        self.keep = keep
        self.id = id
        self.valid = valid
        self.triple = triple
        Dice.instances.append(self)
        
    def ausgabe(self):
        print(f'Es wurde eine {self.wert} geworfen!')
    def setValid(self, valid):
        self.valid = valid
    def setTriple(self,triple):
        self.triple = triple
        
class Players:
    players = []
    def __init__(self,id, name,rolls, score):
        """Das Spielerobjekt. Wird für jeden Mitspieler eingerichtet.
        - Enthält den Namen des Spielers und seine ID 
        - Wie oft er schon geworfen hat (wird nach jeder Runde wieder auf 0 gesetzt)
        - Aktueller Punktestand"""
        self.name = name
        self.id = id
        self.score = score
        self.rolls = rolls
        Players.players.append(self)
        
    def newScore(self, score:int) -> int:
        """Hier wird der neue Score übernommen"""
        self.score = self.score + score
        
class Games:
    def __init__(self,players, turn):
        self.players = players
        self.turn = turn
    