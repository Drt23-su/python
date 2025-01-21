# Cadena para contar las vocales
cadena = "Python es genial"

# Definir las vocales
vocales = "aeiouAEIOU"  # Incluimos tanto minúsculas como mayúsculas

# Contar las vocales en la cadena
contador_vocales = sum(1 for letra in cadena if letra in vocales)

# Imprimir el número de vocales
print(f"La cadena '{cadena}' contiene {contador_vocales} vocales.")