"""Dada la lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista con los cuadrados de los números pares."""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados_pares = [n ** 2 for n in numeros if n % 2 == 0]
print(f"Original: {numeros}")
print(f"Cuadrados pares: {cuadrados_pares}")