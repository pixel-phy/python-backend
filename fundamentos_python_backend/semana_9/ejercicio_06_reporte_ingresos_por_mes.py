"""Reporte de ingresos por mes:
    Del mismo diccionario pedidos (del ejercicio anterior), calcular:
    1. Los ingresos totales agrupados por mes (formato 'YYY-MM')
    2. Muestra los meses ordenados de más reciente a más antiguo.
"""
pedidos = {
    "ORD-001": {
        "cliente": {"nombre": "Ana López", "email": "ana@mail.com", "nivel": "oro"},
        "items": [
            {"producto": "Laptop", "precio": 800, "cantidad": 1},
            {"producto": "Mouse", "precio": 25, "cantidad": 2}
        ],
        "estado": "pendiente",
        "fecha": "2026-05-29"
    },
    "ORD-002": {
        "cliente": {"nombre": "Carlos Ruiz", "email": "carlos@mail.com", "nivel": "plata"},
        "items": [
            {"producto": "Teclado", "precio": 45, "cantidad": 1}
        ],
        "estado": "enviado",
        "fecha": "2026-05-28"
    },

    "ORD-003":{
        "cliente": {"nombre": "Luis Fernández", "email": "luis@mail.com", "nivel": "bronce"},
        "items": [
            {"producto": "monitor", "precio": 200, "cantidad": 1}
            ],
        "estado": "entregado",
        "fecha": "2026-04-15"
    }
}

ingresos_por_mes = {}

for pedido, info in pedidos.items():
    total = 0
    for item in info['items']:
        total += item['precio'] * item['cantidad']
    
    fecha = info['fecha'][:7]

    if fecha not in ingresos_por_mes:
        ingresos_por_mes[fecha] = total
    else:
        ingresos_por_mes[fecha] += total

print("\n--- INGRESOS POR MES ---")
for fecha, valor in ingresos_por_mes.items():
    print(f"{fecha}: {valor}") 
