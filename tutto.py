from helpers.classes import Dice, Players, Games
from helpers.functions import scores, analyzeDiceValue
import random
random.seed()

w = 1

while w <= 6:
    Dice(w,random.randint(1,6),0,1,0)
    w +=1

print(f'Es wurden {len(Dice.instances)} Würfel geworfen!')
counter = 0

#---jetzt folgt die Analyse des Wurfs
#analyzeDices(Dice.instances)
#Diese Liste enthält die Häufigkeit jeder Zahl (von 1 links bis 6 rechts)
values = [0,0,0,0,0,0]
w = 0

for w in range(len(Dice.instances)):
    currentDice = Dice.instances[w]
    if currentDice.keep == 1:
        if currentDice.value == 1:
            values[0] += 1
        elif currentDice.value == 2:
            values[1] += 1
        elif currentDice.value == 3:
            values[2] += 1
        elif currentDice.value == 4:
            values[3] += 1
        elif currentDice.value == 5:
            values[4] += 1
        else:
            values[5] += 1
    w+=1

print(values)

#print(f'Die Zahl 1 kommt {values[0]}x vor')
#print(f'Die Zahl 2 kommt {values[1]}x vor')
#print(f'Die Zahl 3 kommt {values[2]}x vor')
#print(f'Die Zahl 4 kommt {values[3]}x vor')
#print(f'Die Zahl 5 kommt {values[4]}x vor')
#print(f'Die Zahl 6 kommt {values[5]}x vor')

w = 0

# Jetzt gehe ich durch alle Würfel und prüfe mit der values Liste die Häufigkeit ab
# Danach setze ich die Valid und triple Werte
for w in range(len(Dice.instances)):
    currentValue = Dice.instances[w].value
    occurence = values[currentValue - 1]
    if currentValue in (1,5):
        Dice.instances[w].valid = 1
        if occurence == 3:
            Dice.instances[w].triple = 1
    else:
        if occurence >= 3:
            Dice.instances[w].valid = 1
            Dice.instances[w].triple = 1
        else:
            Dice.instances[w].valid = 0
            Dice.instances[w].valid = 0
            Dice.instances[w].keep = 0
    #print(f'W1: {Dice.instances[w].triple}')
    w +=1



#Jetzt wird entschieden, wie das Programm mit den gewürfelten Werten umgeht:
for i, dice in enumerate(Dice.instances):
    #currentDice =  Dice.instances[i]
    aktuellerWert = dice.value
    isTriple = dice.triple
    print(f'Würfel {dice.id} hat den Wert {aktuellerWert}')
    for j, otherDice in enumerate(Dice.instances):
        if i!=j and otherDice.value == dice.value:
            dice.valid == 0

#Nur Informationen über die gewürfelten Werte, kann später wieder gelöscht werden
#for w in range(len(Dice.instances)):
#    print(f'Würfel {w+1}')
#    print(f'Augenzahl: {Dice.instances[w].value}')
#    print(f'Gültig? : {Dice.instances[w].valid}')
#    print(f'Dreier? : {Dice.instances[w].triple}')

    if aktuellerWert in (1,5):
        Dice.instances[i].valid = 1
        counter += 1
    else:
        Dice.instances[i].valid = 0
scoreTotal = 0
score = 0
print('Folgende Werte wurden gewürfelt:')

for i, dice in enumerate(Dice.instances):
    if dice.valid == 1:
        print(f'Würfel {[i+1]} erzielt {scores(i+1,values[i])} Punkte')
        score = score + scores(i+1,values[i])

print(score)

#Aktuellen Wurf eintragen
scoreTotal = score   

print(f'Deine Punkte bisher: {scoreTotal}')
# bevor festgestellt werden kann, welche Würfel behalten werden, muss der Keep Wert überall auf 0 gesetzt werden
for i in range(len(Dice.instances)):
    if Dice.instances[i].valid != 1:
        Dice.instances[i].keep = 0

#print('Wie viele Würfel sollen behalten werden?')
anzahl = int(input('Wie viele Würfel sollen behalten werden?'))
i = 1

while i <= anzahl:
    print("Nenne die Nummer des Würfels:")
    diceNummer = int(input())
    Dice.instances[diceNummer-1].keep = 1
    i += 1
    


print('-----------------------------')
print(f'Insgesamt hast du bereits {scoreTotal} Punkte erwürfelt')
print('.....................')
w = 0
while w <= 5:
    print('Würfel ' + str(Dice.instances[w].id) + ' = ' + str(Dice.instances[w].keep))
    
    w += 1

