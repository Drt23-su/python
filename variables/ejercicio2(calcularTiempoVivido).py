# Declaramos nuestra con la edad
edad = int(input("¿Cuál es tu edad? "))  # Convierte la entrada a un entero


# Calcula meses, días, horas y minutos
meses = edad * 12
dias = edad * 365
horas = dias * 24
minutos = horas * 60

# Imprimir los resultados
print(f"Has vivido aproximadamente:")
print(f"Meses:{meses}")
print(f"Días: {dias}")
print(f"Horas: {horas}")
print(f"Minutos: {minutos}")