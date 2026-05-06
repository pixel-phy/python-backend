"""Dada la matriz:
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

1. Mostrar la matriz.
2. Mostrar cada elemento con su posición.
3. Sumar todos los elementos.
4. Sumar cada fila. 
5. Sumar cada columna."""
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mostrar la matriz
print("\nMostramos la matriz:")
for i in range(len(m)):
    print(f"{m[i]}")

# Mostrar elemento por posición
print("\nElemento con posición:")
for i in range(len(m)):
    for j in range(len(m[i])):
        print(f"fila {i}, columna {j} = {m[i][j]}")

# Suma total
suma_total = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        suma_total += m[i][j]
print(f"\nSuma total: {suma_total}")

# Suma fila
print("\nSuma filas:")
for i in range(len(m)):
    suma_filas = 0
    for j in range(len(m[i])):
        suma_filas += m[i][j]
    print(f"Suma fila {i+1}: {suma_filas}")

# Suma columnas

# Esto es para sumar columnas
c = len(m[0]) # Columnas que conforman la matriz
a = [0] * c # Lista de ceros por columnas para acumular sumas

print("\nSuma columnas:")
for i in range(len(m)):
    for j in range(c):
        a[j] += m[i][j]

for j in range(c):
    print(f"Columna {j}: {a[j]}")
