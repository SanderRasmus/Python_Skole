def filnavn():
    filnavn = input(str("Skriv inn filnavnet: "))
    f_extns = filnavn.split(".")
    print("Filtypen er: " + repr(f_extns[-1]))

filnavn()