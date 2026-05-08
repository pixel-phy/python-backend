"""zip():
Combina dos o más listas pares. Es como cerrar un cierre.
Ejemplo: 
nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]
combinado = list(zip(nombres, edades))
print(combinado) # [('Ana', 25), ('Luis', 30), ('Maria', 28)]

Ejercicio: Dadas las listas:
productos = ["manzana", "pera", "uva"]
precios = [100, 200, 150]

1. Usar zip() para combinarlas.
2. Recorrer el resultado con un for y mostrar: "manzana cuesta $100"."""

productos = ["manzana", "pera", "uva"]
precios = [100, 200, 150]
combinadas = list(zip(productos, precios))
print(combinadas)
for i in combinadas:
    print(f"{i[0]} cuesta ${i[1]}")

# Otra opción:
for producto, precio in zip(productos, precios):
    print(f"\n{producto} cuesta ${precio}")