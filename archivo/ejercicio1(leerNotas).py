# Nombre del archivo
nombre_archivo = 'notas.txt'

try:
    # Abrimos el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        # Leer el contenido del archivo
        contenido = archivo.read()
        # Imprime el contenido en la consola
        print(contenido)
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encontró.")
except Exception as e:
    print(f"Ocurrió un error: {e}")