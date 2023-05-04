navninn = str(input("Hva heter du?: "))
alderinn = int(input("Hvor gammel er du?: "))

def stemmerett(navn, alder):
    if alder >= 18:
        statsborgerskap = str(input("Har du norsk statsborgerskap?: "))
        if statsborgerskap.lower() == "ja":
            print("Du har stemmerett")
        else:
            print("Du har ikke stemmerett")
    else:
        print("Du har ikke stemmerett")

stemmerett(navninn, alderinn)