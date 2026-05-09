"""Dada la matriz = [
                    [100, 200, 150],
                    [80, 210, 130], 
                    [95, 180, 140]],
Calcula:
1. Suma total de todas las ventas.
2. Suma por fila (sucursal).
3. Suma por columna (mes).
4. Venta máxima y su posición (fila, columna)."""

ventas = [
    [100, 200, 150],
    [80, 210, 130],
    [95, 180, 140]
]
print("\nMatriz de ventas:")
for i in range(len(ventas)):
    print(f"Sucursal {i+1}: {ventas[i]}")

print("\n--- SUMA TOTAL ---\n")
suma_total = 0
for i in range(len(ventas)):
    for j in range(len(ventas[i])):
        suma_total += ventas[i][j]

print(f"Total ventas: {suma_total}\n")

print("\n --- SUMA x SUCURSAL ---\n")
for i in range(len(ventas)):
    suma_sucursal = 0
    for j in range(len(ventas[i])):
        suma_sucursal += ventas[i][j]
    print(f"Sucursal {i+1} - Ventas: ${suma_sucursal}")

print("\n --- SUMA x MES ---\n")
meses = len(ventas[0])
sucursales = len(ventas)
acumulador = [0] * meses
for i in range(len(ventas)):
    for j in range(meses):
        acumulador[j] += ventas[i][j]
for j in range(meses):
    print(f"Mes {j+1} - ${acumulador[j]}")

print("\n--- VENTA MÁXIMA ---\n")
maxima = ventas[0][0]
pos_fila = 0
pos_col = 0
for i in range(len(ventas)):
    for j in range(len(ventas[i])):
        if ventas[i][j] > maxima:
            maxima = ventas[i][j]
            pos_fila = i
            pos_col = j

print(f"Venta máxima registrada: sucursal {pos_fila+1} - mes {pos_col+1}")