"""Crear nodos manualmente (sin enlazar)"""

# Paso 1: Definimos los nodos
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Paso 2: Crear nodos sueltos
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

# Paso 3: Mostrar los valores
print(f"nodo1.valor = {nodo1.valor}")
print(f"nodo2.valor = {nodo2.valor}")
print(f"nodo3.valor = {nodo3.valor}")
print(f"nodo1.siguiente = {nodo1.siguiente}")

# Conectar nodo1 con nodo2
nodo1.siguiente = nodo2
print(f"nodo1.siguiente = {nodo1.siguiente}")
print(f"nodo1.siguiente.valor = {nodo1.siguiente.valor}")