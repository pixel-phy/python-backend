""" Clientes inactivos
Un requisito común en Backend es detectar clientes que no han comprado en los últimos X días.

Dado el diccionario pedidos.
1. Encuentra la fecha más reciente de todos los pedidos.
2. Identifica los clientes cuyo único pedido tiene más de 7 días de antigüedad respecto a la fecha más reciente. 
    - Para simplificar, asumimos que cadda día es "01", "02", etc... y comparamos los números.
3. Muestra los nombres y emails de esos clientes. """

pedidos = {
    "ORD-001": {
        "cliente": {"nombre": "Ana López", "email": "ana@mail.com", "nivel": "oro"},
        "items": [{"producto": "laptop", "precio": 800, "cantidad": 1}],
        "estado": "entregado",
        "fecha": "2026-05-29"
    },
    "ORD-002": {
        "cliente": {"nombre": "Carlos Ruiz", "email": "carlos@mail.com", "nivel": "plata"},
        "items": [{"producto": "teclado", "precio": 45, "cantidad": 1}],
        "estado": "entregado",
        "fecha": "2026-05-28"
    },
    "ORD-003": {
        "cliente": {"nombre": "Luis Fernández", "email": "luis@mail.com", "nivel": "bronce"},
        "items": [{"producto": "monitor", "precio": 200, "cantidad": 1}],
        "estado": "entregado",
        "fecha": "2026-05-20"
    },
    "ORD-004": {
        "cliente": {"nombre": "María García", "email": "maria@mail.com", "nivel": "oro"},
        "items": [{"producto": "mouse", "precio": 25, "cantidad": 1}],
        "estado": "entregado",
        "fecha": "2026-05-18"
    }
}

# Encontrar la fecha más reciente
fecha_max = ""

for pedido, info in pedidos.items():
    fecha_actual = info['fecha']

    if fecha_actual > fecha_max:
        fecha_max = fecha_actual

print(f"Fecha más reciente: {fecha_max}")

# Calculamos diferencia de días
fecha_max = "2026-05-29"
fecha_pedido = "2026-05-20"

dia_max = int(fecha_max[-2:])
dia_pedido = int(fecha_pedido[-2:])

diferencia = dia_max - dia_pedido
print(f"Ddiferencia de días: {diferencia}")

# Identificar clientes inactivos
fecha_max = ""
for pedido, info in pedidos.items():
    if info['fecha'] > fecha_max:
        fecha_max = info['fecha']

print("\n--- CLIENTES INACTIVOS ---")
for pedido, info in pedidos.items():
    fecha_pedido = info['fecha']

    dia_max = int(fecha_max[-2:])
    dia_pedido = int(fecha_pedido[-2:])

    diferencia = dia_max - dia_pedido

    if diferencia > 7:
        nombre = info['cliente']['nombre']
        email = info['cliente']['email']
        print(f"{nombre} ({email}) - Último pedido: {fecha_pedido} (hace {diferencia} días)")
