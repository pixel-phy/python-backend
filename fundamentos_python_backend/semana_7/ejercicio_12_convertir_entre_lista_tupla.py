"""Convertir entre lista y tupla
1. Crea una lista: [1, 2, 3, 4, 5]
2. Conviértela a tupla usando tuple().
3. Crea una tupla: (10, 20, 30)
4. Conviértela a lista usando list().
5. Modifica la lista (agrega un elemento) y conviértela de nuevo a tupla."""

lista = [1, 2, 3, 4, 5]
print(f"Lista original: {lista}")
lista_convertida = tuple(lista)
print(f"Lista convertida en tupla: {lista_convertida}")
tupla = (10, 20, 30)
print(f"Tupla original: {tupla}")
tupla_convertida = list(tupla)
print(f"Tupla convertida en lista: {tupla_convertida}")
tupla_convertida[0] = 5
tupla_convertida[2] = 35
segunda_conversion = tuple(tupla_convertida)
print(f"Tupla después de modificaciones: {segunda_conversion}")
