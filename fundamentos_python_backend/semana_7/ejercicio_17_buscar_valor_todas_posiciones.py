"""Buscar valor y mostrar todas las posiciones
Dada una lista enlazada, encuentra todas las posiciones donde aparece un valor.

1. Crear la lista enlazada con los valores: 10, 20, 30, 20, 40, 20, 50.
2. Pedir al usuario un valor a buscar.
3. Recorrer la lista y mostrar todas las posiciones donde aparece.
4. Si el valor no existe, mostrar "❌ Valor no encontrado"."""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)
nodo4 = Nodo(20)
nodo5 = Nodo(40)
nodo6 = Nodo(20)
nodo7 = Nodo(50)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5
nodo5.siguiente = nodo6
nodo6.siguiente = nodo7

try:
    buscar = int(input("Buscar: "))
except ValueError:
    print("❌ Entrada inválida")

cuenta = nodo1
posicion = 0
posiciones = []

while cuenta is not None:
    posicion += 1
    if cuenta.valor == buscar:
        posiciones.append(posicion)
        cuenta = cuenta.siguiente
    else:
        cuenta = cuenta.siguiente
if posiciones:
    if len(posiciones) == 1:
        print(f"El valor {buscar} aparece en la posición {posiciones[0]}")
    else:
        posiciones_str = ", ".join(str(p) for p in posiciones)
        print(f"El valor {buscar} aparece en las posiciones: {posiciones_str}")
else:
    print(f"El valor {buscar} no aparece en la lista enlazada")