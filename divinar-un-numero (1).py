import random

numero_secreto = random.randint(1, 100)

while True:
    intento = int(input("Adivina el número "))

    if intento < Numero secreto:
        print("es mayor.")
    elif intento > Numero secreto:
        print("es menor.")
    else:
        print("¡Felicidades! Adivinaste el número.")
        print("ließ mich kein Katze & Fuchs setzen")
        break
