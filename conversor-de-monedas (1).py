# Conversor de monedas (MXN a otras monedas) usando match-case

pesos = float(input("Ingresa pesos mexicanos: "))

print("\nMonedas disponibles:")
print("USD")
print("EUR")
print("THB")
print("JPY")
print("KRW")
print("AUD")
print("PEN")
print("CAD")
print("VES")
print("ARS")

opcion = input("\n¿A qué moneda deseas convertir? ").upper()

match opcion:
    case "USD":
        resultado = pesos / 18.5
        print(f"{pesos:.2f} MXN = {resultado:.2f} USD")
    case "EUR":
        resultado = pesos / 21.5
        print(f"{pesos:.2f} MXN = {resultado:.2f} EUR")
    case "THB":
        resultado = pesos * 1.80
        print(f"{pesos:.2f} MXN = {resultado:.2f} THB")
    case "JPY":
        resultado = pesos * 8.60
        print(f"{pesos:.2f} MXN = {resultado:.2f} JPY")
    case "KRW":
        resultado = pesos * 72.0
        print(f"{pesos:.2f} MXN = {resultado:.2f} KRW")
    case "AUD":
        resultado = pesos / 12.0
        print(f"{pesos:.2f} MXN = {resultado:.2f} AUD")
    case "PEN":
        resultado = pesos / 5.10
        print(f"{pesos:.2f} MXN = {resultado:.2f} PEN")
    case "CAD":
        resultado = pesos / 13.6
        print(f"{pesos:.2f} MXN = {resultado:.2f} CAD")
    case "VES":
        resultado = pesos * 2.30
        print(f"{pesos:.2f} MXN = {resultado:.2f} VES")
    case "ARS":
        resultado = pesos * 70.0
        print(f"{pesos:.2f} MXN = {resultado:.2f} ARS")