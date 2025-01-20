# Nombre del archivo
nombre_archivo = 'poema.txt'

try:
    # Inicializa el contador de líneas
    contador_lineas = 0
    
    # Abre el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        # Contar las líneas
        for linea in archivo:
            contador_lineas += 1
    
    # Imprime el número de líneas
    print(f"El archivo '{nombre_archivo}' tiene {contador_lineas} líneas.")
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encontró.")
except Exception as e:
    print(f"Ocurrió un error: {e}")