import random

def tilfeldigtall():
    Gjett_Tall = int(input("Vennligst skriv inn et tall mellom 1-10: "))
    Tilfeldigtall = random.randint(0,10)

    while Gjett_Tall != Tilfeldigtall:
        print("Du gjettet", Gjett_Tall)
        print("Det tilfeldiget tallet var", Tilfeldigtall)
        Gjett_Tall = int(input("Vennligst skriv inn et tall mellom 1-10: "))
        Tilfeldigtall = random.randint(0,10)
    else:
        print("Du har gjettet riktig! ")

tilfeldigtall()