"""Buscar por valor y devolver posición:
Dada una lista, encuentra la primera posición donde aparece un valor ingresado por el usuario.

1. Crear una lista con los valores: 10, 20, 30, 40.
2. Pedir al usuario un valor a buscar.
3. Recorrer la lissta y mostrar la posición del primer nodo que contenga ese valor.
4. Si el valor no existe, mostrar "❌ Valor no encontrado"."""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)
nodo4 = Nodo(40)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4

try:
    buscar = int(input("Buscar valor: "))
except ValueError:
    print("❌ Valor inválido!")

posicion = 0
encontrado = False
cuenta = nodo1
while cuenta:
    posicion += 1
    if cuenta.valor == buscar:
        encontrado = True
        break
    cuenta = cuenta.siguiente

if encontrado:
    print(f"El valor {buscar} aparece en la posicón {posicion}")
else:
    print("❌ Valor no encontrado.")