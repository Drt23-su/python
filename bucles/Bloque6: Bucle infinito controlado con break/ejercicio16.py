# Definir la contraseña correcta
contrasena_correcta = "python123"

# Solicitar al usuario que introduzca la contraseña
while True:
    contrasena_usuario = input("Introduce la contraseña: ")
    
    # Verificar si la contraseña es correcta
    if contrasena_usuario == contrasena_correcta:
        print("Contraseña correcta. Acceso concedido.")
        break  # Salir del bucle si la contraseña es correcta
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")