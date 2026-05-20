"""Lista enlazada de coordenadas (ordenar por distancia al origen)
Un sistema de geolocalización maneja puntos en el plano. Cada punto es una tupla (x,y). La lista enlazada debe mantenerse ordenada
por distancia al origen (0,0).
Requisitos:
1. Crear la lista enlazada con los 5 puntos en el orden dado.
2. Mostrar la lista original con coordenadas y distancia.
3. Ordenar la lista por distancia al origen (de menor a mayor) usando el algoritmo de inserción ordenada.
4. Mostrar la lista ordenada."""

class Punto:
    def __init__(self, coordenada):
        self.coordenada = coordenada
        self.siguiente = None

nodo1 = Punto((3, 4))
nodo2 = Punto((1, 1))
nodo3 = Punto((5, 0))
nodo4 = Punto((0, 2))
nodo5 = Punto((4, 3))

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5

# Mostrar lista original
print("--- LISTA ORIGINAL ---")
actual = nodo1
while actual:
    x, y = actual.coordenada
    dist = (x*x + y*y) ** 0.5
    print(f"({x},{y}) Distancia: {dist:.2f}")
    actual = actual.siguiente

# Algoritmo de inserción ordenada
inicio_ordenado = None
original = nodo1  # recorremos la lista original

while original:
    x, y = original.coordenada
    dist_nuevo = x*x + y*y
    
    nuevo = Punto((x, y))
    
    # Insertar al inicio de la nueva lista
    if inicio_ordenado is None:
        nuevo.siguiente = inicio_ordenado
        inicio_ordenado = nuevo
    else:
        x0, y0 = inicio_ordenado.coordenada
        dist_inicio = x0*x0 + y0*y0
        
        if dist_nuevo < dist_inicio:
            nuevo.siguiente = inicio_ordenado
            inicio_ordenado = nuevo
        else:
            actual_ordenado = inicio_ordenado
            while actual_ordenado.siguiente is not None:
                x_sig, y_sig = actual_ordenado.siguiente.coordenada
                dist_sig = x_sig*x_sig + y_sig*y_sig
                if dist_nuevo < dist_sig:
                    break
                actual_ordenado = actual_ordenado.siguiente
            
            nuevo.siguiente = actual_ordenado.siguiente
            actual_ordenado.siguiente = nuevo
    
    original = original.siguiente  # avanzar en la lista original

inicio = inicio_ordenado

print("\n--- LISTA ORDENADA POR DISTANCIA ---")
actual = inicio
while actual:
    x, y = actual.coordenada
    dist = (x*x + y*y) ** 0.5
    print(f"({x},{y}) Distancia: {dist:.2f}")
    actual = actual.siguiente
