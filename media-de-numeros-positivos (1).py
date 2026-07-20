suma = 0
cantidad = 0

while True:
    num = float(input("Ingresa un número: "))

    if num < 0:
        break

    suma += num
    cantidad += 1

if cantidad > 0:
    media = suma / cantidad
    print("La media es:", media)
else:
    print("No se ingresaron")