"""Insertar en una lista enlazada ordenada (Sin utilizar listas auxiliares)
Una lista enlazada debe mantenerse siempre ordenada (de menor a mayor). No se permite usar listas de python auxiliares para ordenar después.
Lista inicial ya ordenada:
10 - 20 - 30 - 40 - 50
Requisitos:
1. Crear la lista enlazada con los valores anteriores.
2. Mostrar la lista actual.
3. Insertar un nuevo valor (pedido al usuario) en la posición correcta para que la lista siga ordenada.
4. Mostrar la lista actualizada.
5. Insertar otro valor (pedido al usuario) y mostrar la lista nuevamente."""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)
nodo4 = Nodo(40)
nodo5 = Nodo(50)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5
nodo5.siguiente = None

inicio = nodo1
print("Lista actual:")
actual = inicio
while actual:
    print(actual.valor, end=" -> " if actual.siguiente else "\n")
    actual = actual.siguiente
try:
    nuevo_valor = int(input("Valor nuevo: "))
    nuevo_nodo = Nodo(nuevo_valor)

    if nuevo_valor < inicio.valor:
        nuevo_nodo.siguiente = inicio
        inicio = nuevo_nodo
    else:
        actual = inicio
        while actual.siguiente is not None and actual.siguiente.valor < nuevo_valor:
            actual = actual.siguiente
        
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo

    print("Lista actualizada:")
    actual = inicio
    while actual:
        print(actual.valor, end=" -> " if actual.siguiente else "\n")
        actual = actual.siguiente
except ValueError as e:
    print(f"Error: {e}")

try:
    otro_valor = int(input("Otro valor: "))
    nuevo_nodo = Nodo(otro_valor)

    if otro_valor < inicio.valor:
        nuevo_nodo.siguiente = inicio
        inicio = nuevo_nodo

    else:
        actual = inicio
        while actual.siguiente is not None and actual.siguiente.valor < otro_valor:
            actual = actual.siguiente

        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo

    print("Lista actualizada:")
    actual = inicio
    while actual:
        print(actual.valor, end=" -> " if actual.siguiente else "\n")
        actual = actual.siguiente

except ValueError as e:
    print(f"Error: {e}")