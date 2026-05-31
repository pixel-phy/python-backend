"""Proyecto integrador: Sistema de Gestión de Pedidos con reportes

Siendo el backend developer de una tienda online te solicitan un sistema de reportes sobre los pedidos del último mes.

Se tiene una lista de pedidos (cada pedido es un diccionario) y se deben generar 4 reportes. 

Reporte 1: ventas totales por nivel de cliente
Agrupa cuánto ha gastado cada nivel (oro, plata, bronce).
Reporte 2: Producto más vendido (en cantidad de unidades).
Calcula cuál producto ha vendido más unidades en total. 
Reporte 3: Método de pago más usado
Cuenta cuántos pedidos usarion cada método de pago (tarjeta, paypal, transferencia).
Reporte 4: Clientes con pedidos pendientes
Lista los nombres y emails de clientes que tienen al menos un pedido con estado "pendiente". Si no hay, muestra "No hay pedidos pendientes"
Reporte 5: Ingresos por día.
Agrupar los ingresos totales por fecha ("YYYY-MM-DD") """

pedidos = [
    {
        "id": "ORD-001",
        "cliente": {"nombre": "Ana López", "email": "ana@mail.com", "nivel": "oro"},
        "items": [
            {"producto": "laptop", "precio": 800, "cantidad": 1},
            {"producto": "mouse", "precio": 25, "cantidad": 2}
        ],
        "estado": "entregado",
        "fecha": "2026-05-29",
        "metodo_pago": "tarjeta"
    },
    {
        "id": "ORD-002",
        "cliente": {"nombre": "Carlos Ruiz", "email": "carlos@mail.com", "nivel": "plata"},
        "items": [
            {"producto": "teclado", "precio": 45, "cantidad": 1}
        ],
        "estado": "enviado",
        "fecha": "2026-05-28",
        "metodo_pago": "paypal"
    },
    {
        "id": "ORD-003",
        "cliente": {"nombre": "Ana López", "email": "ana@mail.com", "nivel": "oro"},
        "items": [
            {"producto": "monitor", "precio": 200, "cantidad": 1}
        ],
        "estado": "entregado",
        "fecha": "2026-05-20",
        "metodo_pago": "tarjeta"
    },
    {
        "id": "ORD-004",
        "cliente": {"nombre": "Luis Fernández", "email": "luis@mail.com", "nivel": "bronce"},
        "items": [
            {"producto": "mouse", "precio": 25, "cantidad": 1},
            {"producto": "mousepad", "precio": 15, "cantidad": 1}
        ],
        "estado": "cancelado",
        "fecha": "2026-05-15",
        "metodo_pago": "transferencia"
    },
    {
        "id": "ORD-005",
        "cliente": {"nombre": "María García", "email": "maria@mail.com", "nivel": "oro"},
        "items": [
            {"producto": "laptop", "precio": 800, "cantidad": 1}
        ],
        "estado": "entregado",
        "fecha": "2026-05-27",
        "metodo_pago": "tarjeta"
    }
]
# Reporte 1
ventas_por_nivel = {
        "oro": 0,
        "plata": 0, 
        "bronce": 0
    }

for pedido in pedidos:
    total_pedido = 0
    for item in pedido["items"]:
        total_pedido += item["precio"] * item["cantidad"]

    nivel = pedido["cliente"]["nivel"]

    ventas_por_nivel[nivel] += total_pedido

print(f"\n--- REPORTE 1: VENTAS POR NIVEL ---")
print(f"oro: {ventas_por_nivel['oro']}")
print(f"plata: {ventas_por_nivel['plata']}")
print(f"bronce: {ventas_por_nivel['bronce']}")

# Reporte 2
ventas_producto = {}

for pedido in pedidos:
    for item in pedido["items"]:
        producto = item["producto"]
        cantidad = item["cantidad"]

        if producto not in ventas_producto:
            ventas_producto[producto] = cantidad
        else:
            ventas_producto[producto] += cantidad

producto_max = None
cantidad_max = -1

for producto, total in ventas_producto.items():
    if total > cantidad_max:
        cantidad_max = total
        producto_max = producto

print("\n--- REPORTE 2: PRODUCTO MÁS VENDIDO ---")
print(f"{producto_max}: {cantidad_max} unidades")

# REPORTE 3
conteo_pagos = {}

for pedido in pedidos:
    metodo = pedido["metodo_pago"]

    if metodo not in conteo_pagos:
        conteo_pagos[metodo] = 1
    else:
        conteo_pagos[metodo] += 1

metodo_max = None
cantidad_max = -1

for metodo, total in conteo_pagos.items():
    if total > cantidad_max:
        cantidad_max = total
        metodo_max = metodo

print("\n--- REPORTE 3: MÉTODO DE PAGO MÁS USADO ---")
print(f"{metodo_max}: {cantidad_max} pedidos")

# REPORTE 4
clientes_pendientes = {}

for pedido in pedidos:
    if pedido["estado"] == "pendiente":
        email = pedido["cliente"]["email"]
        nombre = pedido["cliente"]["nombre"]

        print(f"Pedido pendiente: {pedido['id']} - {nombre} ({email})")

        clientes_pendientes[email] = nombre

print("\n--- REPORTE 4: CLIENTES CON PEDIDOS PENDIENTES ---")

if len(clientes_pendientes) == 0:
    print("No hay pedidos pendientes")
else:
    for email, nombre in clientes_pendientes.items():
        print(f"{nombre} ({email})")

# REPORTE 5
ingresos_por_dia = {}

for pedido in pedidos:
    total_pedido = 0
    for item in pedido["items"]:
        total_pedido += item["precio"] * item["cantidad"]


    fecha = pedido["fecha"]

    if fecha not in ingresos_por_dia:
        ingresos_por_dia[fecha] = total_pedido
    else:
        ingresos_por_dia[fecha] += total_pedido

print("\n--- ACUMULADO ---")
for fecha, total in ingresos_por_dia.items():
    print(f"{fecha}: {total}")
