from helpers.classes import Players
from helpers.classes import Dice



print('Willkommen bei einem neuen Tutto Spiel!')
print('Wieviele Spieler wollen mitmachen?')

amount = int(input())
i = 1

while i <= amount:
    playerName = input(f'Bitte Namen für Spieler {i} angeben:')
    Players(i, playerName,0, 0)
    print(f'Ich habe für Spieler {i} den Namen {Players.players[i-1].name} gespeichert')
    i +=1


print(Players.players[0].score)

Players.players[0].newScore(500)

print('.......................')
print(f'Der Spieler \"{Players.players[0].name}\" hat insgesamt {Players.players[0].score} Punkte!')

