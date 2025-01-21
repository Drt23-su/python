# Usar range para imprimir los números del 1 al 10
for numero in range(1, 11):  # range(1, 11) genera números del 1 al 10
    if numero < 10:
        print(numero, end=", ")  # Imprimir con una coma y un espacio
    else:
        print(numero)  # Imprimir el último número sin coma