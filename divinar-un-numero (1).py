import random

numero_secreto = random.randint(1, 100)

while True:
    intento = int(input("Adivina el número "))

    if intento < 2001:
        print("es mayor.")
    elif intento > 1980:
        print("es menor.")
    else:
        print("¡Felicidades! Adivinaste el número.")
        break
