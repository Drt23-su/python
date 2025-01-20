# Lista de nombres
nombres = []

# Solicitamos al usuario que ingrese nombres
print("Ingrese nombres (escriba 'fin' para terminar):")

while True:
    nombre = input("Nombre: ")
    if nombre.lower() == 'fin':
        break
    nombres.append(nombre)

# Guarda los nombres en el archivo
nombre_archivo = 'nombres.txt'

try:
    with open(nombre_archivo, 'w') as archivo:
        for nombre in nombres:
            archivo.write(nombre + '\n')
    print(f"Los nombres se han guardado en '{nombre_archivo}'.")
except Exception as e:
    print(f"Ocurrió un error al guardar los nombres: {e}")