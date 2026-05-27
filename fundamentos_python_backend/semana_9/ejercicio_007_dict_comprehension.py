"""Comprensión de diccionarios
¿Qué es dict comprehension?
Es una forma compacta de crear diccionarios a partir de iterables."""

# Crear cuadrados de números
cuadrados = {x: x**2 for x in range(5)}
print(cuadrados)

# 2. Con condición (solo pares)
pares_cuadrados = {x: x**2 for x in range(10) if x % 2 == 0}
print(pares_cuadrados)

# 3. Desde una lista de tuplas
items = [("a", 1), ("b", 2), ("c", 3)]
diccionario = {clave: valor for clave, valor in items}
print(diccionario)

# 4. Invertir diccionario (clave: valor)
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: clave for clave, valor in original.items()}
print(invertido)

# 5. Filtrar diccionario
edades = {"Ana": 25, "Luis": 30, "Carlos": 18, "Sofia": 22}
mayores = {nombre: edad for nombre, edad in edades.items() if edad >= 21}
print(mayores)

#Usando dict comprehension:
# 1. Crea un diccionario de los números del 1 al 10 con sus cubos
cubos = {x: x**3 for x in range(11)}
print(cubos)

# 2. Crea un diccionario solo con los números impares del 1 al 10 y sus cuadrados
impares_cuadrados = {x: x**2 for x in range(11) if x % 2 != 0}
print(impares_cuadrados)

# 3. Dada la lista nombres = ["Ana", "Luis", "Carlos"], crea un diccionario donde la clave sea el nombre y el valor sea la longitud
nombres = ["Ana", "Luis", "Carlos"]
diccionario = {nombre: len(nombre) for nombre in nombres}
print(diccionario)

# 4. Dado precios = {"manzana": 100, "pera": 80, "uva": 150}, crea un nuevo diccionario con los precios con 10% de descuento
precios = {"manzana": 100, "pera": 80, "uva": 150}
precios_descuento = {producto: precio * (1 - 0.1) for producto, precio in precios.items()}
print(precios_descuento)
