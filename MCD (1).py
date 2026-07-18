def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


num1 = int(input("primer número: "))
num2 = int(input("segundo número: "))

resultado = calcular_mcd(num1, num2)

print("resultado:", resultado)