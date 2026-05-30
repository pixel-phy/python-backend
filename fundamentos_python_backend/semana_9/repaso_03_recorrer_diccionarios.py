"""Recorrer diccionarios"""

# Formas fundamentales
usuario = {"nombre": "Ana", "email": "ana@mail.com", "edad": 25}

# Forma 1: recorrer claves
for clave in usuario:
    print(clave, "->", usuario[clave])

# Forma 2: recorrer claves explícitamente (igual que arriba)
for clave in usuario.keys():
    print(clave)

# Forma 3: recorrer valores
for valor in usuario.values():
    print(valor)

# Forma 4: recorrer clave + valor (la más común)
for clave, valor in usuario.items():
    print(f"\n{clave}: {valor}")

