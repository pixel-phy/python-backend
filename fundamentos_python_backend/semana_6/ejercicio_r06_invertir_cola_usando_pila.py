"""Invertir lista usando pila
Tenemos la lista [1, 2, 3, 4, 5] y quieres invertirla usando una pila sin aplicar [::-1]."""

lista = [1, 2, 3, 4, 5]
invertida = []

print(f"Lista original: {lista}")

while lista:
    invertida.append(lista.pop())

print(f"Lista invertida: {invertida}")