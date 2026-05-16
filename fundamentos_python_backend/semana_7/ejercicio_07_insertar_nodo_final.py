"""Insertar nodo al final:
Para insertar al final, se recorre hasta el último nodo y allí se enlaza con el nuevo."""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)
nodo4 = Nodo(40)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4

actual = nodo1
while actual:
    print(actual.valor)
    actual = actual.siguiente