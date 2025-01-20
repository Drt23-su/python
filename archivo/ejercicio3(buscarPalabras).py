# Nombre del archivo
nombre_archivo = 'articulo.txt'

# Solicitamos al usuario que ingrese la palabra a buscar
palabra_a_buscar = input("Ingrese la palabra que desea buscar: ")

try:
    # Inicia el contador de ocurrencias
    contador_ocurrencias = 0
    
    # Abrimos el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        # Leer el contenido del archivo línea por línea
        for linea in archivo:
            # Contar cuántas veces aparece la palabra en la línea
            contador_ocurrencias += linea.lower().count(palabra_a_buscar.lower())
    
    # Imprime el número de ocurrencias
    print(f"La palabra '{palabra_a_buscar}' aparece {contador_ocurrencias} veces en el archivo '{nombre_archivo}'.")
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encontró.")
except Exception as e:
    print(f"Ocurrió un error: {e}")