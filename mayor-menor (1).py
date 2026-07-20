numeros = []
datos = 2

for i in range(2):
    dato = input("ponga un numero")
    dato = int(dato)
    numeros.append(dato)

print("mayor:", max(numeros))
print("menor:", min(numeros))