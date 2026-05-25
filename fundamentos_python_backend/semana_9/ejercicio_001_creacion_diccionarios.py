"""Creación de diccionarios
¿Qué es un diccionario?
- Colección de pares clave: valor.
- Las claves son únicas e inmutables (strings, números, tuplas).
- Los valores pueden ser cualquier tipo (números, strings, listas, otros diccionarios).
"""

# 1. Con llaves
usuario = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
print(usuario)

# 2. Con dict()
producto = dict(nombre="Laptop", precio=800, stock=10)
print(producto)

# 3. Diccionario vacío
vacio = {}
vacio2 = dict()
print(vacio, vacio2)

#4. Con pares clave-valor usando zip()
claves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 25, "Madrid"]
persona = dict(zip(claves, valores))
print(persona)

"""Crear los siguientes diccionarios:"""
libro = {"titulo": "Más allá del bien y del mal", "autor": "Nietzsche", "año": 1860, "precio": 230000}
config = {"host": "migue07", "port": "BD_Mongo", "debug": 43523}
datos = {}
datos.update({"nuevo": "valor"})
print(datos)