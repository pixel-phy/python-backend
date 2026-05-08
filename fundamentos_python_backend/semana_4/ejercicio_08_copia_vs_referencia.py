"""Copia vs Referencia:
Cuando asignas una lista a otra variable, no estás copiando, estás creando una referencia.
Por ejemplo:
a = [1, 2, 3]
b = a # esta es la misma lista que a.
b.append(4) # Esto también afecta a la lista a.

para copiar de verdad:
b = a.copy() así si modifico b, a no cambia.

1. Escribir un programa que demuestre el problema de la referencia.
2. Luego muestra cómo solucionarlo."""

lista = [5, 6, 7, 8 , 9]
referencia = lista
referencia.append(10)
print(lista) # Esto afecta a la lista original  'lista'

# Solución
lista1 = [5, 6, 7, 8, 9]
copia = lista1.copy()
copia.append(10)
print(f"Esta es la lista original: {lista1}")
print(f"Esta es la copia de la lista: {copia}")