"""Proyecto integrador semana 8: Sets
Un colegio necesita un sistema para gestionar cursos y estudiantes, usando exclusivamente sets y listas.
Requisitos:
1. Mostrar todos los estudiantes y los cursos que cursa.
2. Mostrar todos los cursos disponibles. 
3. Pedir un curso, mostrar qué estudiantes lo cursan.
4. Agregar nuevo estudiante. Pedir nombre y cursos (separados por comas), crear set de cursos.
5. Agregar curso a estudiante. Pedir estudiante (por índice o nombre) y curso, agregar a su set.
6. Eliminar curso de estudiante. Pedir estudiante y curso, eliminar de su set.
7. Mostrar cursos sin estudiantes. Cursos que no están en ningún set de estudiante.
8. Mostrar estudiantes que cursan todas las materias. Estudiantes cuyo set de cursos es igual al set total de cursos.
9. Mostrar materias más populares.
10. Salir."""

# Cursos disponibles
cursos = {"Matemáticas", "Lengua", "Ciencias", "Historia", "Arte"}

# Estudiantes y sus cursos (usando listas paralelas)
nombres = ["Ana", "Luis", "Carlos", "Sofia", "Juan"]
cursos_por_estudiante = [
    {"Matemáticas", "Lengua"},
    {"Matemáticas", "Ciencias"}, 
    {"Lengua", "Historia", "Arte"},
    {"Matemáticas", "Lengua", "Ciencias"},
    {"Arte"}
]

while True:
    print("\n--- SISTEMA DE GESTIÓN DE CURSOS ---")
    print("1. Mostrar todos los estudiantes")
    print("2. Mostrar todos los cursos")
    print("3. Mostrar estudiantes por curso")
    print("4. Agregar nuevo estudiante")
    print("5. Agregar curso a estudiante")
    print("6. Eliminar curso de estudiante")
    print("7. Mostrar cursos sin estudiantes")
    print("8. Mostrar estudiantes que cursan todas las materias")
    print("9. Mostrar materias más populares")
    print("10. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        print("\n --- LISTA DE ESTUDIANTES ---")
        for i in range(len(nombres)):
            estudiante = nombres[i]
            cursos_estudiante = cursos_por_estudiante[i]

            cursos_str = ", ".join(cursos_estudiante)
            print(f"{i+1}. {estudiante}: {cursos_str}")
    
    elif opcion == "2":
        print("\n--- CURSOS DISPONIBLES ---")
        for curso in cursos:
            print(curso)

        print(f"Total: {len(cursos)} cursos")

    elif opcion == "3":
        print("\n--- ESTUDIANTES POR CURSO ---")
        curso_buscar = input("Ingrese el nombre del curso: ").strip()

        if curso_buscar not in cursos:
            print(f"El curso '{curso_buscar}' no existe en el sistema")
        else:
            estudiantes_en_curso = []

            for i in range(len(nombres)):
                if curso_buscar in cursos_por_estudiante[i]:
                    estudiantes_en_curso.append(nombres[i])

            if estudiantes_en_curso:
                print(f"\nEstudiantes que cursan {curso_buscar}:")
                for estudiante in estudiantes_en_curso:
                    print(f"{estudiante}")
            else:
                print(f"\nNo hay estudiantes cursando {curso_buscar}")

            print(f"Total: {len(estudiantes_en_curso)} estudiantes")

    elif opcion == "4":
        print("\n--- AGREGAR NUEVO ESTUDIANTE ---")

        nombre = input("Nombre del estudiante: ").strip()

        if nombre in nombres:
            print(f"Ya existe un estudiante con el nombre '{nombre}'")
        else:
            cursos_entrada = input("Cursos: ").strip()
            cursos_nuevos = set()
            for curso in cursos_entrada.split(','):
                curso_limpio = curso.strip()
                if curso_limpio:
                    cursos_nuevos.add(curso_limpio)

            cursos_invalidos = set()
            for curso in cursos_nuevos:
                if curso not in cursos_nuevos:
                    cursos_invalidos.add(curso)

            if cursos_invalidos:
                print(f"Los siguientes cursos no existen: {cursos_invalidos}")
                print(f"Cursos válidos: {cursos}")
            else:
                nombres.append(nombre)
                cursos_por_estudiante.append(cursos_nuevos)
                print(f"Estudiante: '{nombre}' agregado exitosamente con {len(cursos_nuevos)} cursos.")
        
    elif opcion == "5":
        print("\n---AGREGAR CURSO A ESTUDIANTE ---")
        print("Estudiantes disponibles:")
        for i in range(len(nombres)):
            print(f"{i}. {nombres[i]}")

        seleccion = input("\nIngrese nombre o índice del estudiante: ").strip()

        indice = None

        if seleccion.isdigit():
            indice = int(seleccion)
            if indice < 0 or indice >= len(nombres):
                print(f"Índice inválido")
                indice = None
        else:
            for i in range(len(nombres)):
                if nombres[i] == seleccion:
                    indice = i
                    break
            
            if indice is None:
                print(f"No se encontró estudiante: '{seleccion}'")

        if indice is not None:
            curso = input("Curso a agregar: ").strip()

            if curso not in cursos:
                print(f"El curso '{curso}' no existe en el sistema")
            elif curso in cursos_por_estudiante[indice]:
                print(f"{nombres[indice]} ya cursa {curso}")
            else:
                cursos_por_estudiante[indice].add(curso)
                print(f"Curso '{curso}' agregado a {nombres[indice]}")

    elif opcion == "6":
        print("\n--- ELIMINAR CURSO DE ESTUDIANTE ---")
        print("Estudiantes disponibles:")
        for i in range(len(nombres)):
            print(f"{i}. {nombres[i]}")

        seleccion = input("\nIngrese nombre o índice del estudiante: ").strip()

        indice = None
        if seleccion.isdigit():
            indice = int(seleccion)
            if indice < 0 or indice >= len(nombres):
                print(f"Índice inválido")
                indice = None
        else:
            for i in range(len(nombres)):
                if nombres[i] == seleccion:
                    indice = i
                    break

            if indice is None:
                print(f"No se encontró estudiante '{seleccion}'")

        if indice is not None:
            print(f"\nCursos actuales de {nombres[indice]}:")
            for curso in cursos_por_estudiante[indice]:
                print(f"{curso}")

            curso = input("\nCurso a eliminar: ").strip()

            if curso not in cursos_por_estudiante[indice]:
                print(f"{nombres[indice]} no cursa {curso}")
            else:
                cursos_por_estudiante[indice].discard(curso)
                print(f"Curso '{curso}' eliminado de {nombres[indice]}")

    elif opcion == "7":
        print("--- CURSOS SIN ESTUDIANTES ---")
        cursos_con_estudiantes = set()

        for cursos_set in cursos_por_estudiante:
            cursos_con_estudiantes.update(cursos_set)

        cursos_sin_estudiantes = cursos - cursos_con_estudiantes

        if cursos_con_estudiantes:
            print("Cursos sin estudiantes:")
            for curso in cursos_sin_estudiantes:
                print(f"{cursos}")
            else:
                print("Todos los cursos tienen al menos un estudiante")

            print(f"Total: {len(cursos_sin_estudiantes)} cursos")

    elif opcion == "8":
        print("--- ESTUDIANTES QUE CURSAN TODAS LAS MATERIAS ---")
        estudiantes_todas = []

        for i in range(len(nombres)):
            if cursos_por_estudiante[i] == cursos:
                estudiantes_todas.append(nombres[i])

        if estudiantes_todas:
            print("Estudiantes que cursan todas las materias:")
            for estudiante in estudiantes_todas:
                print(f"{estudiante}: {len(cursos)} cursos")
        else:
            print("No hay estudiantes que cursen todas las materias")

        print(f"Total: {len(estudiantes_todas)} estudiantes")

    elif opcion == "9":
        
        print("\n--- MATERIAS MÁS POPULARES ---")
        lista_cursos = list(cursos)
        conteo = []
        
        for curso in lista_cursos:
            contador = 0
            for cursos_est in cursos_por_estudiante:
                if curso in cursos_est:
                    contador += 1
            conteo.append(contador)
        
        max_estudiantes = max(conteo) if conteo else 0
        
        if max_estudiantes > 0:
            print(f"Cursos con mayor cantidad de estudiantes ({max_estudiantes} estudiantes):")
            for i in range(len(lista_cursos)):
                if conteo[i] == max_estudiantes:
                    print(f"  - {lista_cursos[i]}")
        else:
            print("No hay estudiantes registrados")
            
    elif opcion == "10":
        print("\nHasta luego!")
        break
    
    else:
        print("Opción inválida. Por favor seleccione una de las opciones del menú.")


