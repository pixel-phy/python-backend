"""Buscar y modificar valor de un nodo
Dada una lista enlazada, busca la primera ocurrencia de un valor y cámbialo por otro.
Lista inicial: 10 -> 20 -> 30 -> 20 -> 40 

1. Crear una lista enlazada con los valores.
2. Pedir al usuario el valor a buscar.
3. Pedir al usuario el nuevo valor.
4. Buscar la primera ocurrencia del valor y cambiarlo por el nuevo valor.
5. Mostrar la lista antes y después del vambio."""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)
nodo4 = Nodo(20)
nodo5 = Nodo(40)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5

try:
    buscar = int(input("Buscar: "))
    nuevo = int(input("Nuevo valor: "))
except ValueError:
    print("❌ Búsqueda o valor nuevo inválidos")
    exit()

cuenta = nodo1
lista_original = []
while cuenta:
    lista_original.append(cuenta.valor)
    cuenta = cuenta.siguiente

lista_original_str = " -> ".join(str(i) for i in lista_original)
print(f"Lista original: {lista_original_str}")

cuenta = nodo1
encontrado = False

while cuenta is not None:
    if cuenta.valor == buscar:
        cuenta.valor = nuevo
        encontrado = True
        break
    cuenta = cuenta.siguiente

if encontrado:
    
    lista_cambiada = []
    cuenta = nodo1
    while cuenta:
        lista_cambiada.append(cuenta.valor)
        cuenta = cuenta.siguiente
    lista_cambiada_str = " -> ".join(str(i) for i in lista_cambiada)
    print(f"✅ Lista modificada: {lista_cambiada_str}")
else:
    print(f"❌ El valor {buscar} no aparece en la lista")
    