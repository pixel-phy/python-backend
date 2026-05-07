"""Búsqueda en listas: index() e in
Dada la lista numeros = [5, 2, 8, 2, 9, 1, 5, 5]
1. Verifica si 8 está en la lista.
2. Encuentre la posición del primer 5.
3. Encuentre cuántas veces aparece 5 en la lista.
4. Encuentra la posición del segundo 5."""

numeros = [5, 2, 8, 2, 9, 1, 5, 5]
print(8 in numeros)
print(numeros.index(5))
print(numeros.count(5))
print(numeros.index(5, 1))