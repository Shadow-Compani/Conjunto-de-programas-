mayores = 0
menores = 0
iguales = 0

n = int(input("¿Cuántos números vas a ingresar? "))

for i in range(n):
    numero = float(input(f"Ingrese el número {i + 1}: "))

    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1

print("\nResultados:")
print("Mayores que cero:", mayores)
print("Menores que cero:", menores)
print("Iguales a cero:", iguales)