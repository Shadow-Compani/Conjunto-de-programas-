def calcular_descuento(precio):
    if precio <= 100:
        descuento = 0.05   
    elif precio <= 200:
        descuento = 0.10   
    elif precio <= 500:
        descuento = 0.15  
    else:
        descuento = 0.20   

    precio_final = precio * (1 - descuento)
    return precio_final

precio = float(input("Ingrese el precio: "))

resultado = calcular_descuento(precio)

print(f"Precio final con descuento: ${resultado:.2f}")