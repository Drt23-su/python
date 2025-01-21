# Diccionario de productos y precios
productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}

# Calcular la suma total de los precios
suma_total = sum(productos.values())

# Imprimir la suma total
print(f"Suma total de los precios: {suma_total}")

# Valor dado para filtrar productos
valor_dado = 1.0

# Crear una lista de productos cuyo precio sea mayor que el valor dado
productos_mayores = [producto for producto, precio in productos.items() if precio > valor_dado]

# Imprimir la lista de productos
print(f"Productos con precio mayor que {valor_dado}: {productos_mayores}")