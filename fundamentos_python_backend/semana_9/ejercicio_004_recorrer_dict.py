# Recorrer diccionarios
# ¿Cómo se recorren diccionarios en python?

usuario = {"nombre": "Ana", "edad": 25, "ciudad": "madrid"}

print(f"Diccionario principal: {usuario}")

# 1. Recorrer solo las claves 
print("\n=== Claves ===")
for clave in usuario:
    print(clave)

# 2. Recorrer solo los valores
print("\n=== Valores ===")
for valor in usuario.values():
    print(valor)

# 3. Recorrer claves y valores (forma 1)
print("\n=== Clave y valor (con corchetes) ===")
for clave in usuario:
    print(f"{clave}: {usuario[clave]}")

# 4. Recorrer claves y valores (forma 2)
print("\n === Clave y valor (con items) ===")
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# Ejercicio
libro = {"titulo": "Más allá del bien y del mal", "autor": "Nietzsche", "año": 1653, "editorial": "Norma"}

# Recorrer claves e imprimirlas
print("\n--- CLAVES ---")
for clave in libro:
    print(clave)

# Recorrer valores e imprimirlos
print("\n--- VALORES ---")
for valor in libro.values():
    print(valor)

# Recorrer claves y valores
print("\n--- CLAVES Y VALORES ---") 
for clave, valor in libro.items():
    print(f"{clave}: {valor}")

