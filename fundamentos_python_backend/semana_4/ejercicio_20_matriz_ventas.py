""" Matriz de ventas:

Una tienda tiene 3 sucursales y registró ventas durante 4 días.

1. Mostrar la matriz como tabla.
2. Calcular total vendido por sucursal.
3. Calcular total vendido por día.
4. Mostrar cuál sucursal vendió más en total. """

ventas = [
    [100, 200, 150, 90],
    [80, 210, 130, 110],
    [95, 180, 140, 120]
]
# Mostramos la matriz como tabla
print("\nVentas por sucursal y días:")
for i in range(len(ventas)):
    print(f"Sucursal {i+1}: {ventas[i]}")

# Total por sucursal (filas)
print("\n --- Total por sucursal ---")
for i in range(len(ventas)):
    total_sucursal = 0
    for j in range(len(ventas[i])):
        total_sucursal += ventas[i][j]
    print(f"Sucursal {i+1}: ${total_sucursal}")

#Total por día (columnas)
print("\n--- Total por día ---")
dias = len(ventas[0])

for j in range(dias):
    total_dia = 0
    for i in range(len(ventas)):
        total_dia += ventas[i][j]
    print(f"Día {j+1}: ${total_dia}")

# Sucursal que más vendió
max_ventas = -1
sucursal_max = -1
print("\n--- Sucursal que más vendió ---")
for i in range(len(ventas)):
    total_sucursal = 0
    for j in range(len(ventas[i])):
        total_sucursal += ventas[i][j]
    if total_sucursal > max_ventas:
        max_ventas = total_sucursal
        sucursal_max = i + 1

print(f"La sucursal que más vendió fue la sucursal {sucursal_max} con ${max_ventas}")
            
