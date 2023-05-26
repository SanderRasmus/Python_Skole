def kalkulator():
    valg = int(input("Velg en av de følgene: "))

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
        
kalkulator()