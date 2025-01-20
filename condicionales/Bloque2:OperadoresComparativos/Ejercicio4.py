# Pedimos al usuario que ingrese los dos números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Comparamos los números y mostramos el resultado correspondiente
if numero1 > numero2:
    print("El primer número es mayor que el segundo.")
elif numero2 > numero1:
    print("El segundo número es mayor que el primero.")
else:
    print("Ambos números son iguales.")


