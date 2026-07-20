peso = float(input("peso"))
altura = float(input("altura"))

imc = peso / (altura**2)

print("imc", imc)
if imc < 18.5:
    print("bajo peso")
elif 18.5 <= imc <= 24.9:
    print("normal")
elif 25 <= imc <= 29.9:
    print("gorda")   
else:
    print("rasputia")