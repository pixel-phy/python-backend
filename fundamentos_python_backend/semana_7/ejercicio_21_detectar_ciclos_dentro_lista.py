"""Detectar si la lista tiene un ciclo (Algoritmo de la liebre y la tortuga):
Una lista enlazada puede tener un ciclo (un nodo que apunta hacia atrás). Debes detectar si existe un ciclo.
Requisitos:
1. Crear dos listas:
- Una sin ciclo (normal).
- Una con ciclo (el último apunta al tercero, por ejemplo)
2. Detectar si hay ciclo usando algoritmo de Floyd (liebre y tortuga):
- Dos punteros: tortuga (avanza 1 paso) y liebre (avanza 2 pasos).
- Si se encuentran: hay ciclo
- Si la liebre llega a None: no hay ciclo"""

class Lista:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Nodos de la lista 1
nodo1_primera = Lista(10)
nodo2_primera = Lista(20)
nodo3_primera = Lista(30)
nodo4_primera = Lista(40)
nodo5_primera = Lista(50)

# Definimos punteros de la lista 1
nodo1_primera.siguiente = nodo2_primera
nodo2_primera.siguiente = nodo3_primera
nodo3_primera.siguiente = nodo4_primera
nodo4_primera.siguiente = nodo5_primera
nodo5_primera.siguiente = nodo3_primera

# Nodos de la lista 2
nodo1_segunda = Lista(10)
nodo2_segunda = Lista(20)
nodo3_segunda = Lista(30)
nodo4_segunda = Lista(40)
nodo5_segunda = Lista(50)

# Definimos punteros de la lista 2
nodo1_segunda.siguiente = nodo2_segunda
nodo2_segunda.siguiente = nodo3_segunda
nodo3_segunda.siguiente = nodo4_segunda
nodo4_segunda.siguiente = nodo5_segunda
nodo5_segunda.siguiente = None

# Mostramos las listas y hacemos validación con algoritmo de Floyd
# Primera lista
tortuga = nodo1_primera
liebre = nodo1_primera
ciclo = False
print("Lista 1 (con cliclo):")
while liebre is not None and liebre.siguiente is not None:
    tortuga = tortuga.siguiente
    liebre = liebre.siguiente.siguiente
    
    if tortuga == liebre:
        ciclo = True
        break

if ciclo:
    print("✅ Si hay ciclo")
else:
    print("❌ No hay ciclo")
    
# Segunda lista
tortuga = nodo1_segunda
liebre = nodo1_segunda
ciclo = False
print("Lista 2 (sin cliclo):")
while liebre is not None and liebre.siguiente is not None:
    tortuga = tortuga.siguiente
    liebre = liebre.siguiente.siguiente
    
    if tortuga == liebre:
        ciclo = True
        break
    
if ciclo:
    print("✅ Si hay ciclo")
else:
    print("❌ No hay ciclo")