# Lista de números
numeros = [10, 15, 20, 25, 30]

# Creamos una nueva lista para los números pares
numeros_pares = []

# Usamos un bucle para filtrar los números pares
for numero in numeros: #Esto es para que nos recorra los numeros
    if numero % 2 == 0:  # Verificar si el número es par
        numeros_pares.append(numero)  # Agregar a la lista de números pares

# Imprime la nueva lista de números pares
print("Números pares:", numeros_pares)