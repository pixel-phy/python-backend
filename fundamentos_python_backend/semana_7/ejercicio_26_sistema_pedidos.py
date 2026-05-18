"""Sistema de pedidos (Cola de prioridad con tuplas y lista enlazada):
Una cafetería recibe pedidos. Cada pedido tiene:
- Número de pedido.
- Nombre del cliente.
- Bebida.
- Prioridad (True, False).

cada pedido tiene una tupla: (id, cliente, bebida, urgente)

Lista inicial: [
                (1, "Ana", "Café", False)
                (2, "Luis", "Té", False)
                (3, "Carlos", "Jugo", True)   # urgente
]
Requisitos:
1. Crear la lista enlazada con los 3 pedidos.
2. Mostrar todos los pedidos en orden de llegada.
3. Reordenar la lista para que los pedidos urgentes queden la inicio (respectando el orden de llegada entre urgentes)
    - Urgentes primero (en orden de llega)
    - Normales después (en orden de llegada)
4. Mostrar la lista reordenada.
5. Atender el primer pedido (se elimina de la lista)
6. Mostrar la lista después de atender."""

class Pedidos:
    def __init__(self, pedido):
        self.pedido = pedido
        self.siguiente = None

# Crear nodos
p1 = Pedidos((1, "Ana", "Café", False))
p2 = Pedidos((2, "Luis", "Té", False))
p3 = Pedidos((3, "Carlos", "Jugo", True))

# Enlazar
p1.siguiente = p2
p2.siguiente = p3

print("\n--- PEDIDOS ORIGINALES ---")
actual = p1
while actual:
    tipo = "Urgente" if actual.pedido[3] else "Normal"
    print(f"{actual.pedido[0]}. {actual.pedido[1]} - {actual.pedido[2]} ({tipo})")
    actual = actual.siguiente

# Separar urgentes y normales (manteniendo orden)
urgentes = []
normales = []
actual = p1
while actual:
    if actual.pedido[3]:
        urgentes.append(actual.pedido)
    else:
        normales.append(actual.pedido)
    actual = actual.siguiente

# Reconstruir lista enlazada: urgentes primero, luego normales
todos = urgentes + normales
if not todos:
    p1 = None
else:
    p1 = Pedidos(todos[0])
    actual = p1
    for pedido in todos[1:]:
        actual.siguiente = Pedidos(pedido)
        actual = actual.siguiente

print("\n--- PEDIDOS REORDENADOS ---")
actual = p1
while actual:
    tipo = "Urgente" if actual.pedido[3] else "Normal"
    print(f"{actual.pedido[0]}. {actual.pedido[1]} - {actual.pedido[2]} ({tipo})")
    actual = actual.siguiente

# Atender primer pedido
print("\n--- ATENDIENDO PRIMER PEDIDO ---")
if p1:
    atendido = p1
    p1 = p1.siguiente
    print(f"✅ Atendido: {atendido.pedido[1]} - {atendido.pedido[2]}")

print("\n--- PEDIDOS RESTANTES ---")
actual = p1
if not actual:
    print("No hay pedidos pendientes")
while actual:
    tipo = "Urgente" if actual.pedido[3] else "Normal"
    print(f"{actual.pedido[0]}. {actual.pedido[1]} - {actual.pedido[2]} ({tipo})")
    actual = actual.siguiente