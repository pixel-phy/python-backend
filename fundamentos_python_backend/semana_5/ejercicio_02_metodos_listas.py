"""Métodos de listas:
Dada la lista numeros = [5, 2, 8, 2, 9, 1, 5, 5], realiza las siguientes operaciones:
1. Muestra la lista original.
2. Agrega el número 3 al final usando append().
3. Cuenta cuántas veces aparece el número 5.
4. Encuentra la posición del primer 2.
5. Ordena la lista de menor a mayor.
6. Invierte la lista usando reverse().
7. Elimina el último elemento y muestra cuál fue.
8. Muestra la lista final. """

numeros = [5, 2, 8, 2, 9, 1, 5, 5]
print(f"Original: {numeros}")
numeros.append(3)
print(f"Lista con 3: {numeros}")
aparece_5 = numeros.count(5)
print(f"El número 5 aparece: {aparece_5} veces")
posicion_2 = numeros.index(2)
print(f"El índice del primer 2: {posicion_2}")
numeros.sort()
print(f"De menor a mayor: {numeros}")
numeros.reverse()
print(f"Invertida: {numeros}")
elimina_ultimo = numeros.pop()
print(f"Elemento {elimina_ultimo} eliminado")
print(f"Lista final: {numeros}")