
def scores(value:int, amount:int) -> int:
    """value ist hier die gewürfelte Zahl und amount die Häufigkeit im aktuellen Wurf"""
    if value > 6:
        return 0
    else:
        if amount < 3:
            if value == 5:
                result = value * 10
            elif value == 1:
                result = value * 100
            else:
                result = 0
        elif amount >= 3:
            if value == 1:
                result = value * 1000
            else:
                result = value * 100
        else:
            result = 0
    
    return result

def analyzeDiceValue(diceValue, occurence):
    """Der erste Wert ist die Zahl auf dem Würfel (1 bis 6)
    Der 2. Wert ist die Häufigkeit.
    Bei 1 und 5 kann er auch einmal vorkommen, bei allen anderen Zahlen muss er 3x vorkommen"""
    if diceValue in (1,5):
        if occurence == 0:
            result = f"Die {diceValue} ist nicht vorgekommen"
        elif occurence == 3:
            result = f"Die {diceValue} ist 3x vorgekommen"
        
        

    # Das return Objekt sollte ein Tupel sein:
    # (3,1) wären dann alle Würfel mit der 3 wären ein Triple, deswegen ist der 2. Wert eine 1        
    return result
    
    
    
