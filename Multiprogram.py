import random

def choose():
    print("Tilgjengelige programmer: \n [1] Gjett Tall 1-10 \n [2] Gjett Tall 1-100 \n [3] Celsius / Fahrenheit Kalkulator \n [4] Bakventskrift \n [5] Kalkulator")
    chooseprogram = int(input("Velg en av programene ovenfor: "))

    if chooseprogram == 1:
        tilfeldigtall()
    if chooseprogram == 2:
        tilfeldigtall_v2()
    if chooseprogram == 3:
        temperatur_konvertor()
    if chooseprogram == 4:
        bakventskrift()
    if chooseprogram == 5:
        kalkulator()
    if chooseprogram < 1:
        print("Du har valgt et program som ikke eksisterer, vennligst prøv på nytt")
    if chooseprogram > 5:
        print("Du har valgt et program som ikke eksisterer, vennligst prøv på nytt")


def tilfeldigtall():
    Gjett_Tall = int(input("Vennligst gjett et tall mellom 1-10: "))
    Tilfeldigtall = random.randint(0,10)

    while Gjett_Tall != Tilfeldigtall:
        print("Du gjettet", Gjett_Tall)
        print("Det tilfeldige tallet var", Tilfeldigtall)
        Gjett_Tall = int(input("Vennligst gjett et tall mellom 1-10: "))
        Tilfeldigtall = random.randint(0,10)
    else:
        print("Du har gjettet riktig!")

def tilfeldigtall_v2():
    guess = int(input("Vennligst gjett et tall mellom 0-100:  "))
    random_number = random.randint(0,99)

    while guess != random_number:
        if guess > random_number:
            print("Du har gjettet for høyt! Prøv igjen med et lavere tall")
        else:
            print("Du har gjettet et tall som er for lavt! Prøv igjen!")
        guess = int(input("Vennligst gjett et tall mellom 0-100:  "))
    print("Gratulerer du har gjettet riktig")

def temperatur_konvertor():
    temperatur = float(input("Hvilken temperatur ønsker du å omgjøre?: "))
    målingsenhet = str(input("Er temperaturen i målenheten C eller F?: "))

    if målingsenhet.upper() == "C":
        temperatur = temperatur * 1.8 + 32
        print("Temperaturen er", temperatur, "I Farenheit")
    elif målingsenhet.upper() == "F":
        temperatur = (temperatur - 32) / 1.8
        print("Temperaturen er", temperatur, "I Celsius")
    else:
        print("Ugyldig måleenhet")

def bakventskrift():
    tekst = str(input("Vennligst skriv ordet/teksten du vil skal komme i baklengs: "))[::-1]

    print(tekst)

def kalkulator(): 
    print("Tilgjengelige regnearter: \n [1] Pluss \n [2] Minus \n [3] Gange \n [4] Dele")
    valg = int(input("Velg en av de følgene prosessene: "))

    if valg == 1:
        number1 = int(input("Velg tall nummer 1: "))
        number2 = int(input("Velg tall nummer 2: "))
        print(number1 + number2)
    if valg == 2:
        number1 = int(input("Velg tall nummer 1: "))
        number2 = int(input("Velg tall nummer 2: "))
        print("Tallet ditt ble:", number1 - number2)
    if valg == 3:
        number1 = int(input("Velg tall nummer 1: "))
        number2 = int(input("Velg tall nummer 2: "))
        print("Tallet ditt ble:", number1 * number2) 
    if valg == 4:
        number1 = int(input("Velg tall nummer 1: "))
        number2 = int(input("Velg tall nummer 2: "))
        print("Tallet ditt ble:", number1 / number2)
    if valg < 1:
        print("Du har valgt et tall for lavt! Vennligst velg mellom 1-4")
    if valg > 4:
        print("Du har valgt et for høyt tall! Velg mellom 1-4")

choose() 
