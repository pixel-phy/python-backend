"""Suma de cada columna
Sumar los elementos de cada columna y mostrar el resultado."""

matriz = [[1, 2, 3],
          [4, 5, 6]]

columnas = len(matriz[0]) # Cuántas columnas tiene la matriz.
sumas_columnas = [0] * columnas # Se crea una lista de 0 con el número de columnas para acumular las sumas.

for i in range(len(matriz)):
    for j in range(columnas):
        sumas_columnas[j] += matriz[i][j]
        
for j in range(columnas):
    print(f"Suma columna {j+1}: {sumas_columnas[j]}")
