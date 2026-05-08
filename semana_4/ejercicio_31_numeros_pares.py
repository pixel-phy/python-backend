"""Dada la lista numeros = [10, 15, 20, 25, 30, 35, 40] crear una nueva lista solo con los números pares."""

numeros = [10, 15, 20, 25, 30, 35, 40]
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]
print(f"\nNúmeros: {numeros}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")