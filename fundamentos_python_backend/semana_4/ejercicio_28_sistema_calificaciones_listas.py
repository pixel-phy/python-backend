"""Sistema de calificacinoes con listas
Un profesor maneja las notas de 5 estudiantes en 3 materias.
1. Mostrar la matriz con formato (índice estudiante y nombre de materia).
2. Calcular el promedio de cada estudiante.
3. Calcular el promedio de cada materia.
4. Encontrar la nota más alta de la matriz, y en qué estudiante/materia está.
5. Mostrar cuántos estudiantes aprobaron cada materia (nota>=60)."""

notas = [
    [85, 90, 78],
    [88, 76, 95],
    [91, 84, 79],
    [70, 65, 80],
    [82, 88, 91]
]

materias = ["Matemáticas", "Lengua", "Ciencia"]

print("\n=== SISTEMA DE CALIFICACIONES ===\n")
# Mostrar la matriz
print("\nNotas registradas:")
for i in range(len(notas)):
    for j in range(len(notas[i])):
        print(f"Estudiante {i+1} materia {materias[j]}: nota {notas[i][j]}")

# Promedio de cada estudiante
cant_estudiantes = len(notas)
cant_materias = len(notas[0])
acumulador = [0] * cant_materias

print("\nPromedios x estudiante")
for i in range(len(notas)):
    suma_estudiante = 0
    for j in range(len(notas[i])):
        suma_estudiante += notas[i][j]
    promedio = suma_estudiante / cant_materias
    print(f"Estudiante {i+1} - Promedio {promedio:.2f}")

# Promedio de cada materia
print("\nPromedio x cada materia")
for i in range(len(notas)):
    for j in range(cant_materias):
        acumulador[j] += notas[i][j]
    
for j in range(cant_materias):
    promedio_materias = acumulador[j] / cant_estudiantes
    print(f"Promedio en {materias[j]} es de {promedio_materias:.2f}")

# Nota más alta
max_nota = notas[0][0]
pos_est = 0
for i in range(len(notas)):
    for j in range(len(notas[i])):
        if notas[i][j] > max_nota:
            max_nota = notas[i][j]
            pos_est = i
            pos_mat = materias[j]

print(f"\nLa nota más alta fue {max_nota}. La sacó el estudiante {pos_est+1} en {pos_mat}")

# Aprobados por materia
aprobados = [0, 0, 0]

for i in range(len(notas)):
    for j in range(len(notas[i])):
        if notas[i][j] >= 60:
            aprobados[j] += 1

print("\nAprobados por materia:")
for j in range(len(materias)):
    print(f"{materias[j]}: {aprobados[j]} estudiantes.")

