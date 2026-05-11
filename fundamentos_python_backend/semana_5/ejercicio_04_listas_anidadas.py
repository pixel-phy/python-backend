"""Matrices:
Dada la matriz: ventas = [
                            [100, 200, 150],
                            [80, 210, 130],
                            [95, 180, 140]
                            ]
Calcular:
1. Suma total de todas las ventas.
2. Suma por sucursal.
3. Suma por mes.
4. Venta máxima y su posición (sucursal, mes).
5. Promedio de ventas por sucursal.
6. Mostrar la matriz con formato bonito."""

ventas = [
    [100, 200, 150],
    [80, 210, 130],
    [95, 180, 140]
]
cant_meses = len(ventas[0])
acum = [0] * cant_meses
cant_sucursales = len(ventas)

# Suma total
suma_total = 0
for i in range(len(ventas)):
    for j in range(len(ventas[i])):
        suma_total += ventas[i][j]
print(f"\nSuma total ventas: ${suma_total}")

# Suma por sucursal
for i in range(len(ventas)):
    suma_sucursal = 0
    for j in range(len(ventas[i])):
        suma_sucursal += ventas[i][j]
    promedio = suma_sucursal / cant_meses    
    print(f"\nSucursal {i+1}:  ${suma_sucursal} - promedio ${promedio:.2f}")

# Suma por mes

for i in range(len(ventas)):
    for j in range(cant_meses):
        acum[j] += ventas[i][j]
for j in range(cant_meses):
    print(f"\nMes {j+1}: ${acum[j]}")

# Venta máxima y posición
maxima = ventas[0][0]
sucursal = 0
mes = 0
for i in range(len(ventas)):
    for j in range(len(ventas[i])):
        if ventas[i][j] > maxima:
            maxima = ventas[i][j]
            sucursal = i
            mes = j
print(f"\nLa venta máxima fue ${maxima} en la sucursal {sucursal+1} el mes {mes+1}")

# Formato bonito
print("\n--- MATRIZ ---")
for i in range(len(ventas)):
    print(f"Sucursal {i+1}: ventas {ventas[i]} ")