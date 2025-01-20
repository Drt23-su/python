# Nombres de los archivos
archivo_origen = 'origen.txt'
archivo_destino = 'destino.txt'

try:
    # Abre el archivo de origen en modo lectura
    with open(archivo_origen, 'r') as origen:
        # Leer el contenido del archivo de origen
        contenido = origen.read()
    
    # Abre el archivo de destino en modo escritura
    with open(archivo_destino, 'w') as destino:
        # Escribe el contenido en el archivo de destino
        destino.write(contenido)
    
    print(f"El contenido de '{archivo_origen}' se ha copiado a '{archivo_destino}'.")
except FileNotFoundError:
    print(f"El archivo '{archivo_origen}' no se encontró.")
except Exception as e:
    print(f"Ocurrió un error: {e}")