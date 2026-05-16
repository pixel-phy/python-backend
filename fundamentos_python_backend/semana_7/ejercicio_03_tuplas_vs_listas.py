"""Tuplas vs Listas
1. Crear una lista y una tupla con los mismos elementos.
2. Modificar el primer elemento de la lista.
3. Intenta modificar el primer elemento de la tupla.
4. Evaluar cuál es más rápida"""

import timeit

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

lista[0] = -4
try:
    tupla[0] = -4
except TypeError as e:
    print(f"Error: {e}")

tiempo_lista = timeit.timeit(f"{lista}", number=1000000)
tiempo_tupla = timeit.timeit(f"{tupla}", number=1000000)

print(f"Tiempo lista: {tiempo_lista:.6f}")
print(f"Tiempo tupla: {tiempo_tupla:.6f}")