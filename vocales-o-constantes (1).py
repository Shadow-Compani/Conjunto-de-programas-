letra = input("Ingresa una letra: ").lower()

if letra in "aeiou":
    print("Vocal ", end="")
elif letra.isalpha() and len(letra) == 1:
    print("Consonante ", end="")
else:
    print("Entrada no válida ", end="")