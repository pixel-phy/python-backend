"""Eliminar un nodo específico (por valor):"""

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

# Mostramos la lista original
actual = nodo1

print("Lista original: ")
while actual:
    print(actual.valor)
    actual = actual.siguiente

# Valor a eliminar
eliminar = 30

# Caso 1: eliminar el primer nodo
if nodo1.valor == eliminar:
    nodo1 = nodo1.siguiente
    print(f"\nEliminado {eliminar} (era el primero)")
else:
    # Buscar el nodo anterior al que queremos eliminar
    actual = nodo1
    while actual.siguiente is not None and actual.siguiente.valor != eliminar:
        actual = actual.siguiente

    if actual.siguiente is not None:
        # Eliminar el nodo saltándolo
        actual.siguiente = actual.siguiente.siguiente
        print(f"Eliminado {eliminar}")
    else:
        print(f"Valor {eliminar} no encontrado")

# Mostrar lista después de eliminar
print(f"\nLista después de eliminar {eliminar}:")
actual = nodo1
while actual:
    print(actual.valor)
    actual = actual.siguiente