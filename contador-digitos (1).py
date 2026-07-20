numero = int(input("Ingresa un número: "))

numero = abs(numero) 

if numero == 0:
    contador = 1
else:
    contador = 0
    while numero > 0:
        numero //= 10
        contador += 1

print("El número tiene", contador, "dígitos.")