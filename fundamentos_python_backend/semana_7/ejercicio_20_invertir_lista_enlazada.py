"""Invertir una lista enlazada (clásico de entrevistas)
Dada una lista enlazada, debes invertir el orden de los nodos (el último pasa a ser primero, el primero pasa a ser el último).
lista inicial: 10 -> 20 -> 30 -> 40 -> 50.
Lista invertida: 50 -> 40 -> 30 -> 20 -> 10

Requisitos:
1. Crear la lista enlazada con los valores: 10, 20, 30, 40, 50.
2. Mostrar la lista original.
3. Invertir la lista (modificando los punteros, no creando una nueva lista)
4. Mostrar la lista invertida."""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)
nodo4 = Nodo(40)
nodo5 = Nodo(50)
# Se crean los apuntadores
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5
# Se muestra la lista enlazada
actual = nodo1
print("\nLista enlazada original: ")
while actual is not None:
    print(actual.valor)
    actual = actual.siguiente
# Invertimos la lista
actual = nodo1
anterior = None

print("\nInvirtiendo la lista...")
while actual:
    siguiente = actual.siguiente
    actual.siguiente = anterior
    anterior = actual
    actual = siguiente         
    
nodo1 = anterior
actual = nodo1
print("\nAsí queda la lista invertida:")
while actual:
    print(actual.valor)
    actual = actual.siguiente