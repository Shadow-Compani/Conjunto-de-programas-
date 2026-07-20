import random

numero_secreto = random.randint(1, 100)

while True:
    intento = int(input("Adivina el número "))

    if intento < numero_secreto:
        print("es mayor.")
    elif intento > numero_secreto:
        print("es menor.")
    else:
        print("¡Felicidades! Adivinaste el número.")
        break