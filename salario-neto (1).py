# Programa para calcular el salario neto

salario_bruto = float(input(" salario bruto: "))
impuestos = float(input("porcentaje de impuestos: "))
deducciones = float(input("deducciones: "))

salario_neto = salario_bruto - (salario_bruto * impuestos / 100) - deducciones

print("El salario es:", salario_neto)