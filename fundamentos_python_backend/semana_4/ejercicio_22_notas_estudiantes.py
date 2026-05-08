"""Notas de 5 estudiantes en 3 exámenes:
notas = [
    [78, 85, 90],
    [62, 70, 68],
    [95, 88, 92],
    [45, 50, 55],
    [80, 85, 87]
]
1. Mostrar la matriz en tabla. 
2. Mostrar posición de cada nota.
3. Suma total de las notas.
4. Suma total por estudiantes.
5. Suma total por exámenes.
6. Nota máxima.
7. Estudiante y examen.
8. Promedio de cada estudiante.
9. Promedio de cada examen."""
notas = [
    [78, 85, 90],
    [62, 70, 68],
    [95, 88, 92],
    [45, 50, 55],
    [80, 85, 87]
]
# Definimos variables
examenes = len(notas[0]) # Cantidad de examenes hechos
acumulador = [0] * examenes # Para acumular las sumas
estudiantes = len(notas)

# Mostramos la matriz
print("\nMatriz:")
for i in range(len(notas)):
    print(notas[i])

# Posición de cada nota
print("\nPosición de cada nota en la matriz:")
for i in range(len(notas)):
    for j in range(len(notas[i])):
        print(f"fila {i+1} columna {j+1}: nota {notas[i][j]}")

# Suma total notas
suma_total = 0
for i in range(len(notas)):
    for j in range(len(notas[i])):
        suma_total += notas[i][j]
print(f"\nTodas la notas suman: {suma_total}")

# Suma por estudiantes aquí podemos calcular el promedio
print("\nSuma por estudiantes:")
for i in range(len(notas)):
    suma_estudiante = 0
    for j in range(len(notas[i])):
        suma_estudiante += notas[i][j]
    promedio = suma_estudiante / examenes
    print(f"Las notas del estudiante {i+1}: suman {suma_estudiante}")
    print(f"Promedio del estudiante {i+1}: {promedio:.2f}\n")

# Suma total por examenes calculamos promedio también
print("\nSuma por exámenes:")
for i in range(len(notas)):
    for j in range(examenes):
        acumulador[j] += notas[i][j]
for j in range(examenes):
    print(f"Examen {j+1}: {acumulador[j]}")
    promedio_examenes = acumulador[j] / estudiantes
    print(f"Promedio examen # {j+1}: {promedio_examenes:.2f}")

# Nota máxima
maxima = notas[0][0]
pos_fila = 0
pos_col = 0
for i in range(len(notas)):
    for j in range(len(notas[i])):
        if notas[i][j] > maxima:
            maxima = notas[i][j]
            pos_fila = i
            pos_col = j
print(f"\nLa nota máxima fue: {maxima}, del estudiante {pos_fila + 1 } en el examen {pos_col + 1 }")


