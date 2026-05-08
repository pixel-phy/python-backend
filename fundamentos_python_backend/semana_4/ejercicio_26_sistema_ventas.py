"""Sistema de ventas
Una tienda registra ventas diarias. Cada venta es un diccionario con:
- "producto" nombre.
- "cantidad" entero.
- "precio_unitario" float.
- "vendedor" nombre
- "fecha" formato yyyy-mm-dd.
1. Mostrar todas las ventas (formato legible).
2. Calcular venta total y mostrar por venta y total acumulado.
3. Calcular total vendido por vendedor.
4. Calcular total vendido por producto.
5. Encontrar el producto más vendido (en cantidad).
6. Filtrar ventas de un día específico (pedir una fecha al usuario y mostrar ventas de ese día).
7. Agregar una nueva venta con validaciones (producto, cantidad > 0, precio > 0, vendedor no vacío, fecha formato)."""

ventas = [
    {"producto": "laptop", "cantidad": 2, "precio_unitario": 800, "vendedor": "Ana", "fecha": "2025-05-01"},
    {"producto": "mouse", "cantidad": 5, "precio_unitario": 25, "vendedor": "Luis", "fecha": "2025-05-01"},
    {"producto": "camiseta", "cantidad": 3, "precio_unitario": 20, "vendedor": "Ana", "fecha": "2025-05-02"},
    {"producto": "laptop", "cantidad": 1, "precio_unitario": 800, "vendedor": "Carlos", "fecha": "2025-05-02"},
    {"producto": "libro python", "cantidad": 4, "precio_unitario": 45, "vendedor": "Luis", "fecha": "2025-05-03"},
    {"producto": "teclado", "cantidad": 3, "precio_unitario": 60, "vendedor": "Ana", "fecha": "2025-05-03"}
]

# 1. Mostrar ventas
print("\n--- VENTAS ---")
for venta in ventas:
    total_venta = venta["cantidad"] * venta["precio_unitario"]
    print(f"{venta['producto']} - {venta['cantidad']} x ${venta['precio_unitario']} = ${total_venta} ({venta['vendedor']}, {venta['fecha']})")

# 2. Total acumulado
total_general = 0
for venta in ventas:
    total_venta = venta["cantidad"] * venta["precio_unitario"]
    total_general += total_venta
print(f"\nTotal acumulado: ${total_general}")

# 3. Total por vendedor
vendedores = []
totales_vendedor = []

for venta in ventas:
    vendedor = venta["vendedor"]
    total_venta = venta["cantidad"] * venta["precio_unitario"]
    
    if vendedor in vendedores:
        indice = vendedores.index(vendedor)
        totales_vendedor[indice] += total_venta
    else:
        vendedores.append(vendedor)
        totales_vendedor.append(total_venta)

print("\n--- TOTAL POR VENDEDOR ---")
for i in range(len(vendedores)):
    print(f"{vendedores[i]}: ${totales_vendedor[i]}")

# 4. Filtrar por fecha
fecha = input("\nFecha (YYYY-MM-DD): ").strip()
ventas_dia = []
total_dia = 0

for venta in ventas:
    if venta["fecha"] == fecha:
        ventas_dia.append(venta)
        total_dia += venta["cantidad"] * venta["precio_unitario"]

if ventas_dia:
    print(f"\n--- VENTAS DEL {fecha} ---")
    for v in ventas_dia:
        print(f"{v['producto']} - {v['cantidad']} x ${v['precio_unitario']} = ${v['cantidad'] * v['precio_unitario']}")
    print(f"Total del día: ${total_dia}")
else:
    print(f"No hay ventas en {fecha}")