def covert_temperature():
    temperature = float(input("Hvilken temperatur er det: "))
    measuring_unit = str(input("Benytter du deg av C eller F: "))

    if measuring_unit.lower() == "C":
        temperature = temperature * 1.8 + 32
        print("Temperaturen Er", temperature, "I Fahrenheit")
    elif measuring_unit.lower() == "F":
        temperature = (temperature - 32) / 1.8
        print("Temperaturen Er", temperature, "I Celsius")
    else:
        print("Ugyldig måleenhet")

covert_temperature()