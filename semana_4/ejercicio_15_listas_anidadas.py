"""Matriz 2 x 3:
1. Crear una matriz 2 x 3.
2. Utilizar un ciclo for anidado para mostrar cada elemento con su pocisión.
3. Mostrar formato: "fila 0, columna 0: valor"."""

matriz = [[1, 2, 3],
          [4, 5, 6]]

for i in range(len(matriz)): # Filas
    for j in range(len(matriz[i])): # Columnas (Funciona para cualquier tamaño de matriz)
        print(f"fila {i}, columna {j}: {matriz[i][j]}")