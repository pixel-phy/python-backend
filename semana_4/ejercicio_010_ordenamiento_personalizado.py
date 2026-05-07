"""Ordenamiento personalizado (sort() con key)
Dada la lista frutas = ["manzana", "pera", "uva", "sandia", "kiwi"]
1. Ordena alfabéticamente (normal, sin key)
2. Ordena por longitud (de menor a mayor)
3. Ordena por la última letra de cada fruta (key = lambda x: x[-1])
4. Ordena alfabéticamente, pero en orden inverso (de la Z a la A)"""

frutas = ["manzana", "pera", "uva", "sandia", "kiwi"]
print(f"Lista original: {frutas}")
frutas.sort()
print(f".sort(): {frutas}")
frutas.sort(key = len)
print(f".sort(len()): {frutas}")
frutas.sort(key = lambda x: x[-1])
print(f".sort(key = lambda x: x[-1]): {frutas}")
frutas.sort(reverse= True)
print(f"Orden inverso: {frutas}")