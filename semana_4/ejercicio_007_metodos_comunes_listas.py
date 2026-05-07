"""Dada la lista:
lista = [1, 2, 3], realiza las siguientes operaciones en orden.
1. Usa append(4) y muestra la lista.
2. Usa extend([5,6]) y muestra la lista.
3. Usa insert(0,0) y muestra la lista.
4. Usa append([7,8]) y muestra la lista."""

lista = [1, 2, 3]
print(f"\nLista original: {lista}")
lista.append(4)
print(f".append(4): {lista}")
lista.extend([5,6])
print(f".extend: {lista}")
lista.insert(0, 0)
print(f".insert(0,0): {lista}")
lista.append([7,8])
print(f".append(): {lista}")
