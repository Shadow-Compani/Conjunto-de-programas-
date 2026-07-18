palabra = input("Ingrese una palabra: ")

palabra_invertida = ""

for caracter in palabra:
    palabra_invertida = caracter + palabra_invertida

if palabra == palabra_invertida:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")