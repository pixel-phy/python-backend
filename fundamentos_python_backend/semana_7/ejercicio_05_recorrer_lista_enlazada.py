"""Recorrer lista enlazada:
Recorrer una lista desde el principio hasta el final."""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)
nodo4 = Nodo(40)
nodo5 = Nodo(50)

# Conectamos los nodos en secuencia
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5

# Recorrer desde nodo1
actual = nodo1
while actual is not None:
    print(f"Valor: {actual.valor}")
    actual = actual.siguiente

print("Fin de la lista")