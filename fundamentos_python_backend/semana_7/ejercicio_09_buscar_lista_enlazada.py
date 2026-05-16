"""Buscar un valor en una lista enlazada"""

class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Nodo(5)
nodo2 = Nodo(10)
nodo3 = Nodo(20)
nodo4 = Nodo(30)
nodo5 = Nodo(40)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5

#Valor a buscas
buscar = 20
#Recorrer la lista buscando el valor
actual = nodo1
encontrado = False
posicion = 0

while actual is not None:
    posicion += 1
    if actual.valor == buscar:
        encontrado = True
        break
    actual = actual.siguiente

if encontrado:
    print(f"Valor {buscar} encontrado en la posición {posicion}")
else:
    print(f"Valor {buscar} no encontrado")