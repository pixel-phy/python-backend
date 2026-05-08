"""List comprehension: Comprensión de listas
Una forma compacta de crear listas a partir de otras listas.
sintaxis:
nueva = [expresion for elemento in lista if condicion]
Ejemplo:
numeros = [1, 2, 3, 4, 5]
pares = [n for n in numeros if n % 2 == 0].

Ejercicio: 
1. Crear una lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
2. Usando list comprehension:
- lista de números pares.
- lista de números impares.
- lista de cada número elevado al cuadrado.
3. Mostrar las 3 listas resultantes."""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [p for p in numeros if p % 2 == 0]
numeros_impares = [i for i in numeros if i % 2 != 0]
cuadrados = [n ** 2 for n in numeros]

print(f"Números pares: {numeros_pares}")
print(f"Números impares: {numeros_impares}")
print(f"Elementos al cuadrado: {cuadrados}")