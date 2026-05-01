"""Suma de filas de una matriz:
Un programa que sume los valores de cada "fila" en una matriz 3 x 3.
Requisitos:
- Crear una cuadrícula con números fijos."""

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(3):  # filas
    suma = 0
    for j in range(3):  # columnas
        suma += matriz[i][j]
    print(f"Suma fila {i+1}: {suma}")