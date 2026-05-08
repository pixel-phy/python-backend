"""Usando texto = "Python Backend 2025", extraer: 
1. Cada 2 caracteres.
2. Los caracteres en posiciones pares.
3. Los caracteres en posiciones impares."""
print("\n === SLICING EN STRINGS ===\n")
texto = "Python Backend 2025"
cada_dos_caracteres = texto[::2]
posiciones_pares = texto[::2]
posiciones_impares = texto[1::2]

print("\n --- RESULTADOS ---\n")
print(f"Cada 2 caracteres: {cada_dos_caracteres}")
print(f"Caracteres pares: {posiciones_pares}")
print(f"Caracteres impares: {posiciones_impares}")
