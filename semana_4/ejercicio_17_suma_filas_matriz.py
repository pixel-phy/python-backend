"""Suma de cada fila
Sumar los elementos de cada fila y mostrar el resultado"""

matriz = [[1, 2, 3],
          [4, 5, 6]]

for i in range(len(matriz)):
    suma_fila = 0
    for j in range(len(matriz[i])):
        suma_fila += matriz[i][j]
    
    print(f"Suma fila {i+1}: {suma_fila}")