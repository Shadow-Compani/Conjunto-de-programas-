celsius = float(input("Ingresa la temperatura en grados Celsius: "))
opcion = input("¿Convertir a Fahrenheit (F) o Kelvin (K)? ").upper()

match opcion:
    case "f":
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} °C = {fahrenheit:.2f} °F")
    case "k":
        kelvin = celsius + 273.15
        print(f"{celsius} °C = {kelvin:.2f} K")
    case _:
        print("Opción no válida. Escribe 'F' o 'K'.")