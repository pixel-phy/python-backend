"""Sistema de gestión de pedidos de un e-commerce
Eres el desarrollador Backend de una tienda Online. Tienes un diccionario que representa los pedidos del día, donde:
    - Cada pedido tiene un ID único.
    - Cada pedido contiene:
    - "cliente": diccionario con "nombre", "email", "nivel" (bronce, plata y oro)
    - "items": lista de diccionarios, cada uno con "producto", "precio", "cantidad"
    - "estado": puede ser "pendiente", "enviado", "entregado", "cancelado"
    - "fecha": string en formato "YYYY-MM-DD". """

from math import inf

pedidos = {
        "ORD-001":{
            "cliente": {"nombre": "Ana López", "email": "ana@mail.com", "nivel": "oro"},
            "items": [
                {"producto": "laptop", "precio": 800, "cantidad": 1},
                {"producto": "mouse", "precio": 25, "cantidad": 2},
                ],
            "estado": "pendiente",
            "fecha": "2026-05-29"
            },
        "ORD-002": {
            "cliente": {"nombre": "Carlos Ruiz", "email": "carlos@mail.com", "nivel": "plata"},
            "items": [
                {"producto": "teclado", "precio": 45, "cantidad": 1}
                ],
            "estado": "enviado",
            "fecha": "2026-05-28"
            }
        }

""" Calcular y mostrar para cada pedido:
    1. El ID del pedido.
    2. El nombre del cliente.
    3. El total del pedido (suma de precio * cantidad de cada item) """
print("\n --- PEDIDOS GENERADOS ---")
for pedido, info in pedidos.items():
    total = 0
    for item in info['items']:
        total += item['precio'] * item['cantidad']

    print(f"Pedido: {pedido} | Cliente: {info['cliente']['nombre']} | Total: {total}")

""" Mostrar solo los pedidos que estén en estado "pendiente" (ignorar los que estén en estado "enviado", "entregado", "cancelado")
Para cada pedido pendiente, mostrar:
    - ID del pedido
    - Nombre del cliente
    - Total del pedido """

print("\n--- PEDIDOS PENDIENTES ---")
for pedido, info in pedidos.items():
    total = 0
    
    if info['estado'] == "pendiente":
        for item in info['items']:
            total += item['precio'] * item['cantidad']
        print(f"Pedido: {pedido} | Cliente: {info['cliente']['nombre']} | Total: {total}")
    
""" Agrupar pedidos por nivel del cliente:
    Queremos saber cuánto ha gastado cada nivel de cliente (bronce, plata, oro) en total entre todos los pedidos.

    Crear un diccionario llamado ventas_por_nivel que:
    - Las claves sean los niveles ("oro", "plata", "bronce")
    - Los valores sean la suma total de todos los pedidos de clientes de ese nivel """

ventas_por_nivel = {"oro": 0, "plata": 0, "bronce": 0}
print("\n--- VENTAS POR NIVEL ---")
for pedido, info in pedidos.items():
    total = 0
    for item in info['items']:
        total += item['precio'] * item['cantidad']
    
    nivel = info['cliente']['nivel']
    ventas_por_nivel[nivel] += total

for nivel, ventas in ventas_por_nivel.items():
    print(f"{nivel}: {ventas}")

""" Cliente que más gastó
encontrar el nombre del cliente que más dinero ha gastado en total (sumando todos sus pedidos). """

gastos_por_cliente = {}

for pedido, info in pedidos.items():
    total = 0
    for item in info['items']:
        total += item['precio'] * item['cantidad']
    
    email = info['cliente']['email']
    nombre = info['cliente']['nombre']

    if email not in gastos_por_cliente:
        gastos_por_cliente[email] = {"nombre": nombre, "total": total}
    else:
        gastos_por_cliente[email]["total"] += total

email_max = None
max_gasto = -1

for email, datos in gastos_por_cliente.items():
    if datos["total"] > max_gasto:
        max_gasto = datos["total"]
        email_max = email
        nombre_max = datos["nombre"]

print(f"\n--- CLIENTE QUE MÁS GASTÓ ---")
print(f"{nombre_max} ({email_max}) con {max_gasto}")

""" 1. Calcular total de unidades vendidas por producto (sumar cantidades).
2. El producto más vendido. """

ventas_producto = {}

for pedido, info in pedidos.items():
    total = 0
    for item in info['items']:
        producto = item['producto']
        cantidad = item['cantidad']

    if producto not in ventas_producto:
        ventas_producto[producto] = cantidad
    else:
        ventas_producto[producto] += cantidad

producto_max = None
max_cantidad = -1

for producto, cantidad in ventas_producto.items():
    if cantidad > max_cantidad:
        max_cantidad = cantidad
        producto_max = producto

print(f"\n--- UNIDADES VENDIDAS POR PRODUCTO ---")
for producto, cantidad in ventas_producto.items():
    print(f"{producto}: {cantidad}")

print(f"\nProducto más vendido: {producto_max} ({max_cantidad} unidades)")
