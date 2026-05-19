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

# Creamos los nodos
pedido1 = Pedidos((1, "Ana", "Café", False))
pedido2 = Pedidos((2, "Luis", "Té", False))
pedido3 = Pedidos((3, "Carlos", "Jugo", True))

# Punteros de enlace
pedido1.siguiente = pedido2
pedido2.siguiente = pedido3
pedido3.siguiente = None

# Mostramos lista de pedido original
print("\n--- PEDIDOS ORIGINALES ---")
actual = pedido1
while actual:
    tipo = "Urgente" if actual.pedido[3] else "Normal"
    print(f"{actual.pedido[0]}. {actual.pedido[1]} - {actual.pedido[2]} ({tipo})")
    actual = actual.siguiente

# Separar urgentes y normales
urgentes = []
normales = []
actual = pedido1
while actual:
    if actual.pedido[3]:
        urgentes.append(actual.pedido)
    else:
        normales.append(actual.pedido)
    actual = actual.siguiente

# Reconstruimos lista enlazada con urgentes antes que normales
todos = urgentes + normales

if not todos:
    pedido1 = None
else:
    pedido1 = Pedidos(todos[0])
    actual = pedido1
    for pedido in todos[1:]:
        actual.siguiente = Pedidos(pedido)
        actual = actual.siguiente

print("\n--- PEDIDOS REORDENADOS ---")
actual = pedido1
while actual:
    tipo = "Urgente" if actual.pedido[3] else "Normal"
    print(f"{actual.pedido[0]}. {actual.pedido[1]} - {actual.pedido[2]} ({tipo})")
    actual = actual.siguiente

# Atender primer pedido
print("\n--- Atendiendo primer pedido ---")
if pedido1:
    atendiendo = pedido1
    pedido1 = pedido1.siguiente
    print(f"✅ Atendido: {atendiendo.pedido[1]} - {atendiendo.pedido[2]}")

print("\n--- PEDIDOS RESTANTE ---")
actual = pedido1
if not actual:
    print("No hay pedidos pendientes")
while actual:
    tipo = "Urgente" if actual.pedido[3] else "Normal"
    print(f"{actual.pedido[0]}. {actual.pedido[1]} - {actual.pedido[2]} ({tipo})")
    actual = actual.siguiente