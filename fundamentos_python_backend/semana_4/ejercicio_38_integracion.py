"""Ejercicio integrador:
Un profesor tiene las notas de 3 exámenes para 4 estudiantes.
notas = [
    [85, 90, 78],
    [62, 70, 68],
    [95, 88, 92],
    [45, 50, 55]
]
1. Mostrar la matriz con formato: Estudiante x: [examen 1, examen 2, examen 3].
2. Calcular el promedio de cada estudiante.
3. Calcular el promedio de cada examen.
4. Encontrar la nota más alta y en qué estudiante/examen está.
5. Contar cuántos estudiantes aprobraon cada examen (nota >= 60).
6. Transformar la matriz original: reemplazar cada nota < 60 por un 0 (utilizar comprensión de listas anidadas)."""

notas = [
    [85, 90, 78],
    [62, 70, 68],
    [95, 88, 92],
    [45, 50, 55]
]

print("\n --- Matriz ---")
for i in range(len(notas)):
    print(f"Estudiante {i+1}: {notas[i]}")

print("\n--- Promedio x Estudiante ---")
examenes = len(notas[0])
estudiantes = len(notas)
for i in range(estudiantes):
    suma_estudiante = 0
    for j in range(len(notas[i])):
        suma_estudiante += notas[i][j]
    promedio_estudiante = suma_estudiante / examenes
    print(f"Estudiante {i+1} - Promedio {promedio_estudiante:.2f}")

print("\n--- Promedio x Examen ---")
acumulador = [0] * examenes
for i in range(estudiantes):
    for j in range(examenes):
        acumulador[j] += notas[i][j]
for j in range(examenes):
    promedio_examenes = acumulador[j] / estudiantes
    print(f"Examen {j+1} - Promedio {promedio_examenes:.2f}")

print("\n--- Nota más alta ---")
maxima = [0][0]
pos_fila = 0
pos_col = 0
for i in range(estudiantes):
    for j in range(len(notas[i])):
        if notas[i][j] > maxima:
            maxima = notas[i][j]
            pos_fila = i
            pos_col = j
print(f"Nota más alta {maxima} - Estudiante {pos_fila+1} - Examen {pos_col+1}")

print("\n--- Estudiantes aprobaron ---")
for j in range(examenes):
    aprobados = 0
    for i in range(estudiantes):
        if notas[i][j] >= 60:
            aprobados += 1
    print(f"Examen {j+1}: {aprobados} estudiantes aprobaron")

print("\n--- Matriz transformada ---")
ajuste = [[nota if nota >= 60 else 0 for nota in fila] for fila in notas]
for i in range(len(ajuste)):
    print(f"Estudiante {i+1}: {ajuste[i]}")