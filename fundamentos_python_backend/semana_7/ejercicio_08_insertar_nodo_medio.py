"""Insertar nuevo nodo en medio:
Insertar un nuevo nodo entre el nodo3 y el nodo4."""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)
nodo4 = Nodo(40)
nuevo = Nodo(35)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nuevo.siguiente = nodo3.siguiente
nodo3.siguiente = nuevo

actual = nodo1

while actual:
    print(actual.valor)
    actual = actual.siguiente