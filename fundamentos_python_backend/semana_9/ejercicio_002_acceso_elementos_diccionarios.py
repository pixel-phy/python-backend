"""Acceso a elementos del diccionario
¿Cómo acceder a los valores?
"""
# Diccionario de ejemplo
usuario = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# 1. Acceso con corchetes (si la clave no existe, da error)
print(usuario["nombre"])  # Ana
print(usuario["edad"])    # 25

# 2. Acceso con .get() (si no existe, devuelve None o un valor por defecto)
print(usuario.get("ciudad"))     # Madrid
print(usuario.get("profesion"))  # None
print(usuario.get("profesion", "No especificado"))  # "No especificado"

# 3. Modificar valores existentes
usuario["edad"] = 26
print(usuario)  # {'nombre': 'Ana', 'edad': 26, 'ciudad': 'Madrid'}

# 4. Agregar nuevos pares
usuario["profesion"] = "Ingeniera"
print(usuario)  # {'nombre': 'Ana', 'edad': 26, 'ciudad': 'Madrid', 'profesion': 'Ingeniera'}