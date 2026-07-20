def suma(a,b):
    return a + b
def restar(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    return a / b

def mostrar_menu():
    print("calculadora basica")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("selecciona una opcion")

        if opcion == 's':
            print("grasias")
            break
        num1 = float(input("primer numero"))
        num2 = float(input("segundo numero"))

        if opcion == '1':
            print("resultado", suma(num1,num2))
        if opcion == '2':
                    print("resultado", restar(num1,num2))
        if opcion == '3':
                    print("resultado", multiplicar(num1,num2))
        if opcion == '4':
                    print("resultado", dividir(num1,num2))

main()