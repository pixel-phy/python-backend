"""Nodos (La base de las listas enlazadas)

Una lista enlazada está compuesta por nodos. Cada nodo contiene:
- Un valor (los datos).
- Un puntero al siguiente nodo (siguiente)."""

# Se define lo que es un Nodo
class Nodo:
    def __init__(self, valor): # al crear un nodo, se le da un valor
        self.valor = valor # guardamos el valor
        self.siguiente = None # Inicialmente no apunta a nada

# Se crean los nodos sueltos (conectados)
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

# Enlazar nodos
nodo1.siguiente = nodo2 # nodo1 apunta a nodo2
nodo2.siguiente = nodo3 # nodo2 apunta a nodo3
# nodo3.siguiente ya es None (último)

# Recorrer la lista desde el inicio
actual = nodo1                  # empezamos en el primer nodo
while actual:                   # mientras actual no sea None
    print(actual.valor)         # mostrar el valor del nodo actual
    actual = actual.siguiente   # pasar al nodo siguiente