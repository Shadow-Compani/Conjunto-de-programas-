num = int(input("Ingresa un número: "))

factorial = 1

if num < 0:
    print("El factorial no existe para números negativos.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("El factorial de", num, "es:", factorial)