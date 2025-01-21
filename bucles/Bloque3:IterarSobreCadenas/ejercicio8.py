# Cadena original
cadena = "Hola Mundo"

# Inicializar una cadena vacía para almacenar la cadena invertida
cadena_invertida = ""

# Usar un bucle para invertir la cadena
for letra in cadena:
    cadena_invertida = letra + cadena_invertida  # Agregar cada letra al inicio de la cadena invertida

# Imprimir la cadena invertida
print(f"La cadena invertida es: '{cadena_invertida}'")
