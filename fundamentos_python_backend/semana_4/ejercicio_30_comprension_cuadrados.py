"""Dada la lista numeros = [1, 2, 3, 4, 5]. Crear una nueva lista con los cuadrados de cada número
usando compresión de listas."""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = [n ** 2 for n in numeros]
print(f"Original: {numeros}")
print(f"Cuadrados: {cuadrados}")