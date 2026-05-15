"""Proyecto integrador: Sistema de Gestión Estudiantes
Una escuela necesita un sistema para gestionar sus estudiantes. Cada estudiante tiene:
- Nombre.
- Notas en 3 materias (Matemáticas, lengua y Ciencia).
- Asistencia (porcentaje: 0 a 100).
Requisitos:
1. Mostrar resumen general.
- Mostrar todos los estudiantes, sus notas y asistencias.
- Calcular y mostrar el promedio de cada estudiante.
- Mostrar si cada estudiante está "Aprobado" (nota promedio >= 60) o "Reprobado".
2. Mostrar estadísticas por materia.
- Calcular y mostrar el promedio de cada materia.
- Mostrar la nota más alta y más baja de cada materia.
- Mostrar cuántos estudiantes aprograron cada materia (nota >= 60).
3. Ranking de estudiantes
- Mostrar los estudiantes ordenados por nota promedio (de mayor a menor).
- En caso de empate, ordenar por asistencia.
4. Filtrar estudiantes.
- Promedio >= X
- Asistencia >= X
- Los que aprobaron todas las materias.
- Los que reprobaron alguna materia.
5. Modificar datos.
- Agregar un nuevo estudiante (nombre, 3 notas, asistencia).
- Actualizar las notas de un estudiante existente.
- Actualizar la asistencia de un estudiante."""

print("\n === SISTEMA DE GESTIÓN ESTUDIANTES ===\n")
# Datos iniciales
nombres = ["Ana", "Luis", "Carlos", "Maria", "Sofia"]
notas = [
    [85, 90, 78],
    [62, 70, 68],
    [95, 88, 92],
    [45, 50, 55],
    [88, 92, 87]
]
asistencias = [95, 80, 100, 60, 90]
materias = ["Matemáticas", "Lengua", "Ciencias"]
cant_materias = len(notas[0])
cant_estudiantes = len(notas)
acumulador = [0] * cant_materias
acum_max = [0, 0, 0]
min_notas = notas[0][0]
acum_min = [0, 0, 0]
promedios = []

while True:
    print("\n--- Menú principal ---")
    print("1. Mostrar resumen general")
    print("2. Estadísticas por materia")
    print("3. Ranking de estudiantes")
    print("4. Filtrar estudiantes")
    print("5. Modificar datos")
    print("6. Salir")

    # Ingresar opción
    try:
        opcion = int(input("\nOpción: "))
        if opcion > 6 or opcion < 1:
            print("\n❌ Ingrese alguna de las opciones mostradas.")
            continue
        # Opción 1
        elif opcion == 1:
            print("\n--- RESUMEN GENERAL ---\n")
            for i in range(len(notas)):
                print(f"Estudiante: {nombres[i]}")
                for j in range(len(notas[i])):
                    print("Nota: "
                        f"{materias[j]}: {notas[i][j]}")
                print(f"Asistencia: {asistencias[i]}\n")
            
            print("\n--- PROMEDIO ESTUDIANTES ---\n")
            for i in range(len(notas)):
                suma_estudiante = 0
                for j in range(len(notas[i])):
                    suma_estudiante += notas[i][j]
                promedio_estudiante = suma_estudiante / cant_materias
                if promedio_estudiante < 60:
                    mensaje = "(❌ REPROBADO)"
                else:
                    mensaje = "(✅ APROBADO)"
                print(f"{nombres[i]} - Promedio {promedio_estudiante:.2f} {mensaje}")
                   
        # Opción 2
        elif opcion == 2:
            print("\n--- ESTADÍSTICAS POR MATERIA ---\n")
            
            # Inicializar acumuladores por materia
            suma_materias = [0, 0, 0]
            max_materias = [0, 0, 0]
            min_materias = [100, 100, 100]  # inicializar con un valor alto
            
            for i in range(len(notas)):      # recorrer estudiantes
                for j in range(cant_materias):  # recorrer materias
                    suma_materias[j] += notas[i][j]
                    
                    if notas[i][j] > max_materias[j]:
                        max_materias[j] = notas[i][j]
                    
                    if notas[i][j] < min_materias[j]:
                        min_materias[j] = notas[i][j]
            
            # Mostrar resultados
            for j in range(cant_materias):
                promedio = suma_materias[j] / cant_estudiantes
                print(f"{materias[j]}:")
                print(f"  Promedio: {promedio:.2f}")
                print(f"  Nota máxima: {max_materias[j]}")
                print(f"  Nota mínima: {min_materias[j]}")
            
            # Aprobados por materia
            aprobados = [0, 0, 0]
            for i in range(len(notas)):
                for j in range(len(notas[i])):
                    if notas[i][j] >= 60:
                        aprobados[j] += 1
            
            print("\n--- APROBADOS POR MATERIA ---")
            for j in range(cant_materias):
                print(f"{materias[j]}: {aprobados[j]} estudiantes")
                    
        # Opción 3
        elif opcion == 3:
            print("\n--- RANKING DE ESTUDIANTES (por promedio) ---")
            
            # Calcular promedios
            promedios = []
            for i in range(len(notas)):
                suma = sum(notas[i])
                promedio = suma / cant_materias
                promedios.append(promedio)
            
            # Crear lista de índices ordenados por promedio (mayor a menor)
            indices = list(range(len(nombres)))
            indices.sort(key=lambda i: promedios[i], reverse=True)
            
            # Mostrar ranking
            for puesto, i in enumerate(indices, start=1):
                print(f"{puesto}. {nombres[i]} - Promedio: {promedios[i]:.2f} - Asistencia: {asistencias[i]}%")
                # Opción 4
        elif opcion == 4:
            print("\n--- FILTRAR ESTUDIANTES ---")
            print("1. Filtrar por promedio mínimo")
            print("2. Filtrar por asistencia mínima")
            print("3. Estudiantes que aprobaron todas las materias")
            print("4. Estudiantes que reprobaron alguna materia")
            
            sub_opcion = input("Opción: ")
            
            if sub_opcion == "1":
                minimo = float(input("Promedio mínimo: "))
                print(f"\nEstudiantes con promedio ≥ {minimo}:")
                for i in range(len(nombres)):
                    promedio = sum(notas[i]) / cant_materias
                    if promedio >= minimo:
                        print(f"  {nombres[i]} - {promedio:.2f}")
            
            elif sub_opcion == "2":
                minimo = float(input("Asistencia mínima (%): "))
                print(f"\nEstudiantes con asistencia ≥ {minimo}%:")
                for i in range(len(nombres)):
                    if asistencias[i] >= minimo:
                        print(f"  {nombres[i]} - {asistencias[i]}%")
            
            elif sub_opcion == "3":
                print("\nEstudiantes que aprobaron todas las materias:")
                for i in range(len(nombres)):
                    aprobo_todas = all(nota >= 60 for nota in notas[i])
                    if aprobo_todas:
                        print(f"  {nombres[i]}")
            
            elif sub_opcion == "4":
                print("\nEstudiantes que reprobaron alguna materia:")
                for i in range(len(nombres)):
                    reprobo_alguna = any(nota < 60 for nota in notas[i])
                    if reprobo_alguna:
                        print(f"  {nombres[i]}")
        # Opción 5
        elif opcion == 5:
            print("\n--- MODIFICAR DATOS ---")
            print("1. Agregar nuevo estudiante")
            print("2. Actualizar notas de un estudiante")
            print("3. Actualizar asistencia de un estudiante")
            
            sub_opcion = input("Opción: ")
            
            if sub_opcion == "1":
                nombre = input("Nombre: ").strip()
                if not nombre:
                    print("❌ Nombre no puede estar vacío")
                    continue
                
                nuevas_notas = []
                for materia in materias:
                    nota = float(input(f"Nota en {materia}: "))
                    nuevas_notas.append(nota)
                
                asistencia = float(input("Asistencia (%): "))
                
                nombres.append(nombre)
                notas.append(nuevas_notas)
                asistencias.append(asistencia)
                print(f"✅ Estudiante {nombre} agregado")
            
            elif sub_opcion == "2":
                print("\nEstudiantes disponibles:")
                for i, n in enumerate(nombres):
                    print(f"{i}. {n}")
                
                idx = int(input("Número del estudiante: "))
                if idx < 0 or idx >= len(nombres):
                    print("❌ Índice inválido")
                    continue
                
                print(f"Modificando notas de {nombres[idx]}")
                for j, materia in enumerate(materias):
                    nueva = float(input(f"Nueva nota en {materia} (actual {notas[idx][j]}): "))
                    notas[idx][j] = nueva
                print("✅ Notas actualizadas")
            
            elif sub_opcion == "3":
                print("\nEstudiantes disponibles:")
                for i, n in enumerate(nombres):
                    print(f"{i}. {n} - Asistencia: {asistencias[i]}%")
                
                idx = int(input("Número del estudiante: "))
                if idx < 0 or idx >= len(nombres):
                    print("❌ Índice inválido")
                    continue
                
                nueva_asistencia = float(input(f"Nueva asistencia para {nombres[idx]} (actual {asistencias[idx]}%): "))
                asistencias[idx] = nueva_asistencia
                print("✅ Asistencia actualizada")
        elif opcion == 6:
            print("Adiós!")
            break                     
                    
    except ValueError:
        print("Ingrese una opción válida.")