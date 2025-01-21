# Cadena original
cadena = "Hola a todos"

# Inicializar una cadena vacía para almacenar la nueva cadena sin espacios
cadena_sin_espacios = ""

# Usar un bucle para eliminar los espacios
for letra in cadena:
    if letra != " ":  # Verificar si la letra no es un espacio
        cadena_sin_espacios += letra  # Agregar la letra a la nueva cadena

# Imprimir la nueva cadena sin espacios
print(f"La cadena sin espacios es: '{cadena_sin_espacios}'")