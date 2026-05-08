"""Ordenamiento
Ordenar una lista de números sin usar .sort() (para practicar lógica).
1. Crear numeros = [5, 2, 8, 1, 9, 3]
2. Ordenarla de menor a mayor usando el algoritmo de burbuja.
Objetivo: Aprender ordenamiento manual."""

numeros = [5, 2, 8, 1, 9, 3]
longitud = len(numeros)
print(f"Lista original: {numeros}")
# Recorremos todos los elementos de la lista
for i in range(longitud):
    # Últimos i elementos ya están ordenados
    for j in range(0, longitud - i - 1):
        # Intercambiar si el elemento es mayor que el siguiente
        if numeros[j] > numeros[j+1]:
            numeros[j] , numeros[j+1] = numeros[j+1], numeros[j]

print(f"Lista ordenada: {numeros}")

# Con optimización (más rápido)
numeros = [5, 2, 8, 1, 9, 3]
n = len(numeros)

for i in range(n):
    intercambiado = False
    for j in range(0, n - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
            intercambiado = True
    if not intercambiado:
        break

print(numeros)