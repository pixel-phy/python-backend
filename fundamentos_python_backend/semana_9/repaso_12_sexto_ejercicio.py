""" Ejercicio 6: recorrer diccionarios anidados

Dado el diccionario de inventario por categoría.
1. Recorrer el diccionario y mostrar para cada producto:
    - Categoría
    - Producto
    - Stock
    - Precio """

inventario = {
        "electronica": {
            "laptop": {"stock": 5, "precio": 800},
            "mouse" : {"stock": 15, "precio": 25}
            },
        "hogar": {
            "mesa": {"stock": 3, "precio": 120},
            "silla": {"stock": 8, "precio": 45}
            }
        }
for categoria, producto in inventario.items():
    print(f"Categoría: {categoria}")
    for clave, valor in producto.items():
        print(f" Producto: {clave} | Stock: {valor['stock']} | Precio: {valor['precio']}")
