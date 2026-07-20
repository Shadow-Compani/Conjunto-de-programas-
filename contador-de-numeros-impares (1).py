contador = 0

while True:
    num = int(input("Ingresa un número: "))

    if num == 0:
        break

    if num % 2 != 0:
        contador += 1

print("números impares:", contador)