inicio = int(input("primer número: "))
diferencia = int(input("diferencia: "))
terminos = int(input("términos: "))

contador = 0
numero = inicio

while True:
    print(numero)
    numero += diferencia
    contador += 1

    if contador >= terminos:
        break