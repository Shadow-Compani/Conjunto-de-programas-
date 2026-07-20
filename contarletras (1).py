palabra = input("Ingresa una palabra: ")

contador = 0

for letra in palabra:
    if letra == "a":
        contador += 1

print("La letra 'a' aparece", contador, "veces.")