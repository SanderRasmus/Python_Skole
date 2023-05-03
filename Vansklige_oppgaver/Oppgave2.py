import random

def guess_number():
    guess = int(input("Vennligst gjett et tall mellom 0-100:  "))
    random_number = random.randint(0, 99)

    while guess != random_number:
        if guess > random_number:
            print("Du gjettet før høyt! Prøv igjen ")
        else:
            print("Du gjettet for lavt! Prøv igjen ")
        guess = int(input("Vennligst gjett et tall mellom 0-100:  "))

    print("Gratulerer, du har gjettet riktig!")


guess_number()