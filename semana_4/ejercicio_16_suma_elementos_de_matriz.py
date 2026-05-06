"""Suma de todos los elementos de la matriz
Calcular la suma de todos los elementos de la matriz."""

matriz = [[1, 2, 3],
          [4, 5, 6]]

suma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        suma += matriz[i][j]

print(f"Suma de los elementos: {suma}")