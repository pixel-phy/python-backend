"""Práctica con métodos de listas básicos
Dada la lista [3, 1, 4, 1, 5, 9, 2]
Realiza las siguientes operaciones:
1. Agrega el número 6 al final de la lista.
2. Inserta el número 0 an inicio de la lista. 
3. Elimina el primer 1 de la lista. 
4. Elimina el último elemento de la lista.
5. Encuentra la posición del número 5.
6. Cuenta cuántas veces aparece el número 1 en la lista. 
7. Ordena la lista de menor a mayor.
8 Invierte la lista.
Muestra la lista después de cada operaicón para ver cómo va cambiando."""

print("\n=== Método básicos de listas ===\n")
lista = [3, 1, 4, 1, 5, 9, 2]
print(f"\nLista original: {lista}")
# Agregar elemento a la lista:
lista.append(6)
print(f"\nCon elemento nuevo: {lista}")
# Insertar el número 0 al inicio de la lista
lista.insert(0, 0)
print(f"\nNuevo elemento en la posición 0: {lista}")
# Eliminamos el primer elemento
lista.remove(1)
print(f"\nEliminamos el elemento de la posición 0: {lista}")
# Eliminamos el último elemento:
lista.pop()
print(f"\nSi eliminamos el último elemento: {lista}")
# Encontramos la posición del número 5
print(f"\nEl 5 está en la posición: {lista.index(5)}")
# Cuántas veces aparece un elemento en la lista
print(f"\nEl número 1 está {lista.count(1)} veces en la lista.")
# Ordenamos la lista de menor a mayor
lista.sort()
print(f"\nLa lista ordenada de menor a mayor: {lista}")
# Invertimos la lista
lista.reverse()
print(f"\nLa lista alrevés queda: {lista}")
# Ordenamos de mayor a menor
lista.sort(reverse = True)
print(f"\nLa lista de mayor a menor queda: {lista}")