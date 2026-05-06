"""Se tiene la matriz:
m = [
    [0, 2, 4, 6, 8],
    [1, 3, 5, 7. 9]
    ]
1. Mostrar la matriz.
2. Mostrar cada elemento con su posición.
3. Suma total.
4. Suma por filas.
5. Suma por columas."""
# Definimos la matriz
m = [
    [0, 2, 4, 6, 8],
    [1, 3, 5, 7, 9]
]
# Mostramos la matriz en forma de tabla
print("\nMatriz:")
for i in range(len(m)):
    print(f"{m[i]}")

#Mostrar cada elemento con su posición
print("\nElemento con posición:")
for i in range(len(m)):
    for j in range(len(m[i])): # Aplica para todos los tamaños de matrices
        print(f"Fila {i}, Columna {j}: {m[i][j]}")

# Suma total
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
    print(f"\nSuma fila {i+1}: {suma_filas}")

# Suma columnas
c = len(m[0]) # Revisamos la cantidad de columnas.
a = [0] * c # Creamos lista para acumular suma.

print("\nSuma columnas:")
for i in range(len(m)):
    for j in range(c):
        a[j] += m[i][j]

for j in range(c):
    print(f"Columna {j}: {a[j]}")


