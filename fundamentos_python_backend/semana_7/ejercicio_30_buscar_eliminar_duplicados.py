"""Buscar y eliminar duplicados en lista enlazada
Una lista enlazada tiene elementos que pueden estar repetidos. Debes eliminar los duplicados, dejando solo la primera
aparición de cada valor.
Lista inicial: 10 - 20 - 30 - 20 - 40 - 30 - 50 - 20
Resultado esperado: 10 - 20 - 30 - 40 - 50 
Requisitos:
1. Crear una lista enlazada con los valores: 10, 20, 30, 20, 40, 30, 50, 20
2. Mostrar la original
3. Eliminar los valores duplicados, dejando solo la primera aparición de cada valor.
4. Mostrar la lista sin duplicados."""

class Lista:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Lista(10)
nodo2 = Lista(20)
nodo3 = Lista(30)
nodo4 = Lista(20)
nodo5 = Lista(40)
nodo6 = Lista(30)
nodo7 = Lista(50)
nodo8 = Lista(20)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5
nodo5.siguiente = nodo6
nodo6.siguiente = nodo7
nodo7.siguiente = nodo8
nodo8.siguiente = None

print("\n--- Lista original ---")
actual = nodo1
while actual is not None:
    print(actual.valor, end=" -> " if actual.siguiente else "\n")
    actual = actual.siguiente

# Eliminar valores duplicados recorriendo la lista
actual = nodo1
while actual is not None:
    # Buscar duplicados del valor actual
    runner = actual
    while runner.siguiente is not None:
        if runner.siguiente.valor == actual.valor:
            # Eliminar el duplicado
            runner.siguiente = runner.siguiente.siguiente
        else:
            runner = runner.siguiente
    actual = actual.siguiente

print("\n--- Lista sin duplicados ---")
actual = nodo1
while actual is not None:
    print(actual.valor, end=" -> " if actual.siguiente else "\n")
    actual = actual.siguiente