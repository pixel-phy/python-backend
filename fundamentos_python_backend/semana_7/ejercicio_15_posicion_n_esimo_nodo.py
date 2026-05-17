"""Buscar por posición (n-ésimo nodo)
Tienes una lista enlazada de números y quieres encontrar el valor que está en una posición específica (1 = primer nodo).
Requisitos:
1. Crear una lista enlazada con los valores 10, 20, 30, 40, 50.
2. Pedir al usuario una posición (número entero positivo).
3. Buscar el nodo en esa posición.
4. Mostrar el valor del nodo.
5. Si la posición es mayor que la longitud de la lista, mostrar "❌ Posición no válida"."""

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

try:
    posicion = int(input(f"\nPosición: "))  
    if posicion < 1:
        print("❌ La posición debe ser mayor o igual a 1")
    else:
        actual = nodo1
        contador = 1
        while actual is not None and contador < posicion:
            actual = actual.siguiente
            contador += 1

        if actual is not None:
            print(f"El valor en la posición {posicion} es: {actual.valor}")
        
        else:
            print(f"❌ Posición no válida (la lista tiene {contador - 1} elementos)")

except ValueError:
    print("❌ Ingrese un número válido")


