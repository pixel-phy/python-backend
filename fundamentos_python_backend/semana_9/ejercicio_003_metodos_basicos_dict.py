"""Algunos métodos básicos para diccionarios"""

usuario = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# 1. Obtener todas las claves
claves = usuario.keys()
print(f"Claves: {claves}")

# 2. Obtener todos los valores
valores = usuario.values()
print(f"Valores: {valores}")

# 3. Obtener todos los pares
items = usuario.items()
print(f"Items: {items}")

# 4. Longitud del diccionario
print(f"Cantidad de elementos: {len(usuario)}")
print("\n")

libro = {"titulo": "Crimen y castigo", "autor": "Fiodor Dostoievski", "año": 1872}
# mostrar claves
claves = libro.keys()
print(f"Claves: {claves}")

# mostrar valores
valores = libro.values()
print(f"Valores: {valores}")

# mostrar pares
pares = libro.items()
print(f"Pares: {pares}")

# cantidad de elementos
print(f"Cantidad de elementos: {len(libro)}")