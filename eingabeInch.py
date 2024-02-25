import datetime
import calendar


jahr = int(input("Bitte gib das Jahr an:"))
monat = int(input("Bitte gib den Monat an:"))
tag = int(input("Bitte gib den Tag an:"))
tagOK = True
monatOK = True

if tag < 1 or tag > 31:
    print("Der Tag gehört nicht zum Datum")
    tagOK = False
    
if monat < 1 or monat > 12:
    print("Der Monat gehört nicht zu Datum")
    monatOK = False



if tagOK and monatOK: 
    print(f'Das ist jetzt der aktuelle Monat: {datetime.date(jahr, monat, tag)}')
    lastDay = calendar.monthrange(jahr, monat)[1]
    schaltjahr = 'ja' if jahr % 4 == 0 else 'Nein'
    print(f'Der letzte Tag des Monats ist Tag {calendar.monthrange(jahr, monat)[1]}!')
    if schaltjahr == 'ja':
        print(f'Das Jahr {jahr} ist ein Schaltjahr...')
    else:
        print(f'Das Jahr {jahr} ist kein Schaltjahr...')
    
    



