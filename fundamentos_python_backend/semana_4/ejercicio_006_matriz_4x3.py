"""Matriz 4 x 3:
m = [
    [5, 8, 2],
    [7, 1, 9],
    [4, 6, 3],
    [9, 3, 5]
    ]
    1. Mostrar la matriz.
    2. Mostrar elemento con posición.
    3. Suma total.
    4. Suma por filas.
    5. Suma por columnas.
    6. Encontrar el valor máximo en toda la matriz.
    7. Encontrar la posición en la que se encuentra el valor máximo."""
m = [
    [5, 8, 2],
    [7, 1, 9],
    [4, 6, 3],
    [9, 3, 5]
]

# Mostrar matriz
print("\nMatriz: ")
for i in range(len(m)):
    print(m[i])

# Mostrar elemento con posición
print("\nPosición de cada elemento: ")
for i in range(len(m)):
    for j in range(len(m[i])):
        print(f"fila {i+1} columna {j+1}: elemento {m[i][j]}")

# Suma total de la matriz
suma = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        suma += m[i][j]
print(f"\nSuma total: {suma}")

# Suma por filas
for i in range(len(m)):
    suma_filas = 0
    for j in range(len(m[i])):
        suma_filas += m[i][j]
    print(f"fila {i}: {suma_filas}")

# Suma por columnas
columnas = len(m[0]) # Cuántas columnas tiene la matriz
acumulador = [0] * columnas # Para acumular suma de cada columna

for i in range(len(m)):
    for j in range(columnas):
        acumulador[j] += m[i][j]

for j in range(columnas):
    print(f"\nColumna {j}: {acumulador[j]}")

# Encontrar el valor máximo en la matriz
maximo = m[0][0] # Para almacenar valor máximo
pos_fila = 0 # Para almacenar la posición en la fila
pos_col = 0 # Para guardar la posición en la columna
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] > maximo:
            maximo = m[i][j]
            pos_fila = i
            pos_col = j
print(f"\nMáximo: {maximo} en la fila {pos_fila + 1}, columna {pos_col + 1}")
