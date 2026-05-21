"""Eliminar duplicados de una lista usando SET
Esta es una de las aplicaciones más útiles de los sets en Backend."""

# Lista con duplicados
numeros = [1, 2, 2, 3, 4, 4, 4, 5, 1, 3, 3, 6, 7, 8, 9]
print(f"Lista original: {numeros}")

# Convertir a set para eliminar duplicados
unicos = set(numeros)
print(f"Set sin duplicados: {unicos}")

# Volver a la lista si se necesita orden
lista_sin_duplicados = list(unicos)
print(f"Lista sin duplicados: {lista_sin_duplicados}")