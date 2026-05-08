"""Un profesor tiene las calificaciones de 3 estudiantes en 4 materias.
Mostrar:
1. Mostrar la matriz con formato de tabla (filas y columnas alineadas).
2. Calcular y mostrar el promedio de cada estudiante.
3. Calcular y mostrar el promedio de cada materia.
4. Mostrar la nota más alta de toda la matriz y dónde está.
5. Mostrar la nota más baja de toda la matriz y dónde está."""

calificaciones = [
    [85, 90, 78, 92],
    [88, 76, 95, 89],
    [91, 84, 79, 93]
]
print("\n=================== CALIFICACIONES =================\n")
print("| Español | Matemáticas | Inglés | Ciencias | Estudiante    |")
print(f"|   {calificaciones[0][0]}\t  |    {calificaciones[0][1]}\t|    {calificaciones[0][2]}  |    {calificaciones[0][3]}    | Estudiante 1.|")
print(f"|   {calificaciones[1][0]}\t  |    {calificaciones[1][1]}\t|    {calificaciones[1][2]}  |    {calificaciones[1][3]}    | Estudiante 2.|")
print(f"|   {calificaciones[2][0]}\t  |    {calificaciones[2][1]}\t|    {calificaciones[2][2]}  |    {calificaciones[2][3]}    | Estudiante 3.|")

materias = len(calificaciones[0])
sumas_materias = [0] * materias
estudiantes = len(calificaciones)
calificacion_alta = calificaciones[0][0]
calificacion_baja = calificaciones[0][0]
posicion_fila_alta = 0
posicion_columna_alta = 0
posicion_fila_baja = 0
posicion_columna_baja = 0
nombres_materias = ["Español", "Matemáticas", "Inglés", "Ciencias"]

# Promedio por estudiante, son promedio por filas
for i in range(len(calificaciones)):
    suma_calificacion = 0
    for j in range(len(calificaciones[i])):
        suma_calificacion += calificaciones[i][j]
    promedio = suma_calificacion / materias
    print(f"\nPromedio estudiante {i+1}: {promedio:.2f}")

#Promedio por materias, son promedio de columnas
for i in range(len(calificaciones)):
    for j in range(materias):
        sumas_materias[j] += calificaciones[i][j]

for j in range(materias):
    print(f"\nMateria {j+1}: {sumas_materias[j]/estudiantes:.2f}")

#Nota más alta y más baja de toda la matriz
for i in range(len(calificaciones)):
    for j in range(len(calificaciones[i])):
        if calificaciones[i][j] > calificacion_alta:
            calificacion_alta = calificaciones[i][j]
            posicion_fila_alta = i
            posicion_columna_alta = j
        
        if calificaciones[i][j] < calificacion_baja:
            calificacion_baja = calificaciones[i][j]
            posicion_fila_baja = i 
            posicion_columna_baja = j

print(f"\nNota más alta es {calificacion_alta} ({nombres_materias[posicion_columna_alta]}). Que está en la posición [{posicion_fila_alta}][{posicion_columna_alta}]")
print(f"La nota más baja es {calificacion_baja} ({nombres_materias[posicion_columna_baja]}). Ques está en la posición [{posicion_fila_baja}][{posicion_columna_baja}]")
