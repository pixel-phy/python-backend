"""Encontrar el nodo del medio (sin saber la longitud)
Dada una lista enlazada, encuentra el nodo del medio sin recorrerla dos veces y sin calcular la longitud primero.
Requisitos:
1. Crear una lista enlazada con 5 nodos (impar).
2. Encontrar el nodo del medio usando dos punteros.
3. Mostrar el valor del nodo del medio."""

class Lista():
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Lista(10)
nodo2 = Lista(20)
nodo3 = Lista(30)
nodo4 = Lista(40)
nodo5 = Lista(50)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5
nodo5.siguiente = None

liebre = nodo1
tortuga = nodo1

while liebre is not None and liebre.siguiente is not None:
    tortuga = tortuga.siguiente
    liebre = liebre.siguiente.siguiente

print(f"El nodo del medio es: {tortuga.valor}")