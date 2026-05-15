"""Proyecto integrador: Sistema de Gestión de Biblioteca
Una biblioteca necesita un sistema para gestionar su catálogo de libros y los préstamos a usuarios.

libros = ["Cien años de soledad", "El principito", "1984", "Don Quijote", "La sombra del viento"]
autores = ["Gabriel García Márquez", "Antoine de Saint-Exupéry", "George Orwell", "Miguel de Cervantes", "Carlos Ruiz Zafón"]
anios = [1967, 1943, 1949, 1605, 2001]
disponibles = [True, True, True, True, True]  # True = disponible, False = prestado
prestamos = []  # Lista de tuplas (libro, usuario) - se irá llenando

1. Mostrar catálogo completo:
- Mostrar todos los libros con su información.
- Indicar si está disponible o prestado.
2. Buscar libros:
- Por título (búsqueda parcial, sin distinguir mayúsculas)
- Por autor
- Por año
3. Prestar libro:
- Pedir título del libro y nombre del usuario.
- Verificar que el libro exista y esté disponible.
- Registrar el préstamo en la lista prestamos.
- Cambiar disponible a False.
4. Devolver libro:
- Pedir título del libro.
- Verificar que el libro exista y esté prestado.
- Eliminar el préstamo de la lista prestamos.
- Cambiar disponible a True.
5. Ver préstamos activos:
-Mostrar todos los libros prestados y a qué usuario.
6. Estadísticas:
- Total de libros en la biblioteca.
- Cantidad de libros prestados.
- Cantidad de libros disponibles.
- Libro más antiguo (por año).
7. Menú principal con opciones."""

print("\n=== SISTEMA DE GESTIÓN DE BIBLIOTECA ===\n")

libros = ["Cien años de soledad", "El principito", "1984", "Don quijote", "La sombra del viento"]
autores = ["Gabriel García Márquez", "Antoine de Saint-Exupéry", "George Orwell", "Miguel de Cervantes", "Carlos Ruiz Zafón"]
anios = [1967, 1943, 1949, 1605, 2001]
disponibles = [True, True, True, True, True]
prestamos = []  # lista de tuplas (libro, usuario)

while True:
    print("\n--- Menú principal ---")
    print("1. Mostrar catálogo")
    print("2. Buscar libros")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Ver préstamos activos")
    print("6. Estadísticas")
    print("7. Salir")

    try:
        opcion = int(input("\nOpción: "))
        if opcion < 1 or opcion > 7:
            print("❌ La opción no está en el menú.")
            continue

        # 1. Mostrar catálogo
        elif opcion == 1:
            print("\n--- CATÁLOGO ---")
            for i, libro in enumerate(libros):
                estado = "Disponible" if disponibles[i] else "Prestado"
                print(f"{i+1}. {libro} - {autores[i]} ({anios[i]}) - {estado}")

        # 2. Buscar libros
        elif opcion == 2:
            print("\n--- BUSCAR LIBRO ---")
            print("1. Por título")
            print("2. Por autor")
            print("3. Por año")
            
            try:
                opc_buscar = int(input("\nOpción: "))
                if opc_buscar < 1 or opc_buscar > 3:
                    print("❌ Opción de búsqueda no disponible.")
                    continue

                # Buscar por título
                if opc_buscar == 1:
                    buscar = input("Título: ").strip().lower()
                    encontrados = False
                    for i, libro in enumerate(libros):
                        if buscar in libro.lower():
                            print(f"{i+1}. {libro} - {autores[i]} ({anios[i]}) - {'Disponible' if disponibles[i] else 'Prestado'}")
                            encontrados = True
                    if not encontrados:
                        print("❌ No se encontraron libros con ese título.")

                # Buscar por autor
                elif opc_buscar == 2:
                    buscar = input("Autor: ").strip().lower()
                    encontrados = False
                    for i, autor in enumerate(autores):
                        if buscar in autor.lower():
                            print(f"{i+1}. {libros[i]} - {autor} ({anios[i]}) - {'Disponible' if disponibles[i] else 'Prestado'}")
                            encontrados = True
                    if not encontrados:
                        print("❌ No se encontraron libros de ese autor.")

                # Buscar por año
                elif opc_buscar == 3:
                    buscar = input("Año: ").strip()
                    try:
                        año_buscar = int(buscar)
                        encontrados = False
                        for i, año in enumerate(anios):
                            if año_buscar == año:
                                print(f"{i+1}. {libros[i]} - {autores[i]} ({año}) - {'Disponible' if disponibles[i] else 'Prestado'}")
                                encontrados = True
                        if not encontrados:
                            print("❌ No se encontraron libros de ese año.")
                    except ValueError:
                        print("❌ Año no válido.")
            
            except ValueError:
                print("❌ Opción no válida.")

        # 3. Prestar libro
        elif opcion == 3:
            print("\n--- PRESTAR LIBRO ---")
            titulo = input("Título: ").strip()
            
            # Buscar el libro (sin importar mayúsculas)
            indice = None
            for i, libro in enumerate(libros):
                if libro.lower() == titulo.lower():
                    indice = i
                    break
            
            if indice is None:
                print("❌ El libro no existe.")
                continue
            
            if not disponibles[indice]:
                print(f"❌ '{libros[indice]}' no está disponible.")
                continue
            
            usuario = input("Usuario: ").strip()
            if not usuario:
                print("❌ Usuario no válido.")
                continue
            
            disponibles[indice] = False
            prestamos.append((libros[indice], usuario))
            print(f"✅ '{libros[indice]}' prestado a {usuario}.")

        # 4. Devolver libro
        elif opcion == 4:
            print("\n--- DEVOLVER LIBRO ---")
            titulo = input("Título: ").strip()
            
            # Buscar el libro
            indice = None
            for i, libro in enumerate(libros):
                if libro.lower() == titulo.lower():
                    indice = i
                    break
            
            if indice is None:
                print("❌ El libro no existe.")
                continue
            
            if disponibles[indice]:
                print(f"❌ '{libros[indice]}' no está prestado.")
                continue
            
            # Eliminar de la lista de préstamos
            for j, (l, u) in enumerate(prestamos):
                if l.lower() == titulo.lower():
                    prestamos.pop(j)
                    break
            
            disponibles[indice] = True
            print(f"✅ '{libros[indice]}' devuelto correctamente.")

        # 5. Ver préstamos activos
        elif opcion == 5:
            print("\n--- PRÉSTAMOS ACTIVOS ---")
            if not prestamos:
                print("No hay libros prestados actualmente.")
            else:
                for libro, usuario in prestamos:
                    print(f"📖 {libro} - Prestado a: {usuario}")

        # 6. Estadísticas
        elif opcion == 6:
            print("\n--- ESTADÍSTICAS ---")
            total = len(libros)
            prestados_count = len(prestamos)
            disponibles_count = total - prestados_count
            
            # Libro más antiguo y más reciente
            indice_antiguo = 0
            indice_reciente = 0
            for i in range(len(anios)):
                if anios[i] < anios[indice_antiguo]:
                    indice_antiguo = i
                if anios[i] > anios[indice_reciente]:
                    indice_reciente = i
            
            print(f"Total de libros: {total}")
            print(f"Libros prestados: {prestados_count}")
            print(f"Libros disponibles: {disponibles_count}")
            print(f"Libro más antiguo: '{libros[indice_antiguo]}' ({anios[indice_antiguo]})")
            print(f"Libro más reciente: '{libros[indice_reciente]}' ({anios[indice_reciente]})")

        # 7. Salir
        elif opcion == 7:
            print("Hasta luego!")
            break

    except ValueError:
        print("❌ Ingrese una opción válida.")