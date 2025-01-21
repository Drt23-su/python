# Número para la tabla de multiplicar
numero = 5

# Usar range para generar la tabla de multiplicar del número
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):  # Generar números del 1 al 10
    resultado = numero * i  # Calcular el resultado de la multiplicación
    print(f"{numero} x {i} = {resultado}")  # Imprimir el resultado