"""Transformación de datos para API
En backend es común recibir datos en un formato y tener que transformarlos para enviarlos a otra API o al frontend.

Una tienda Online va a enviar un reporte de pedidos a un sistema externo de logística. El sistema externo espera los datos en otro 
formato.
Formato actual:
pedidos = {
    "ORD-001": {
        "cliente": {"nombre": "Ana López", "email": "ana@mail.com"},
        "items": [
            {"producto": "laptop", "precio": 800, "cantidad": 1},
            {"producto": "mouse", "precio": 25, "cantidad": 2}
        ],
        "estado": "pendiente"
    }
}

Formato que pide la API:
    pedidos_transformados = [
    {
        "id": "ORD-001",
        "cliente_nombre": "Ana López",
        "cliente_email": "ana@mail.com",
        "total": 850,  # suma de precio * cantidad
        "productos": ["laptop", "mouse"],  # solo nombres
        "estado": "pendiente"
    }
]
1. Transformar el diccionario pedidos original en una lista.
2. Cada elemento de la lista debe ser un diccionario con las claves que pide la API externa.
3. Mostrar el resultado final.
"""
pedidos = {
    "ORD-001": {
        "cliente": {"nombre": "Ana López", "email": "ana@mail.com", "nivel": "oro"},
        "items": [
            {"producto": "laptop", "precio": 800, "cantidad": 1},
            {"producto": "mouse", "precio": 25, "cantidad": 2}
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

pedidos_transformados = []

for pedido, info in pedidos.items():
    total = 0
    productos_nombres = []
    for item in info['items']:
        total += item['precio'] * item['cantidad']
        productos_nombres.append(item['producto'])

    nuevo_pedido = {
            "id": pedido,
            "cliente_nombre": info['cliente']['nombre'],
            "cliente_email": info['cliente']['email'],
            "total": total,
            "productos": productos_nombres,
            "estado": info['estado']
            }

    pedidos_transformados.append(nuevo_pedido)

print("\n--- PEDIDOS TRANSFORMADOS PARA API ---")
for pedido in pedidos_transformados:
    print(pedido)



