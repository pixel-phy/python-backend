"""Insertar un nodo al inicio:
Insertar significa que el nuevo nodo ser convierte en el nodo1, y el antiguo nodo1 pasa a ser el segundo."""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Insertar al inicio
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)
nuevo_nodo = Nodo(-20)

nuevo_nodo.siguiente = nodo1
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

actual = nuevo_nodo
while actual:
    print(actual.valor)
    actual = actual.siguiente

