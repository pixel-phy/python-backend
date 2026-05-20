"""Sistema de gestión de Biblioteca
Una biblioteca necesita un sistema para gestionar préstamos de libros. Cada libro tiene:
- Título
- Autor
- Año de publicación
- Disponible (true/false)
Requisitos del sistema: 
1. Agregar libro.
2. Mostrar todos los libros.
3. Buscar libro por título
4. Prestar libro
5. Devolver libro
6. Eliminar libro
7. Ordenar libros por año
8. Ordenar libros por título
9. Mostrar estadísticas
10. Salir"""

# Creamos la estructura de los nodos
class Libro:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None

libro1 = Libro(("Cien años de soledad", "García Márquez", 1967, True))
libro2 = Libro(("El principito", "Saint-Exupéry", 1943, True))
libro3 = Libro(("1984", "Orwell", 1949, True))
libro4 = Libro(("Don Quijote", "Cervantes", 1605, True))
libro5 = Libro(("La sombra del ciento", "Zafón", 2001, True))

# Se definen apuntadores
libro1.siguiente = libro2
libro2.siguiente = libro3
libro3.siguiente = libro4
libro4.siguiente = libro5
libro5.siguiente = None

inicio = libro1
# Mostramos la lista de los libros
print("\n--- LISTA DE LIBROS ---")
actual = inicio
while actual:
    titulo, autor, año, disponible = actual.datos
    estado = "Disponible" if disponible else "Prestado"
    print(f"{titulo} - {autor} ({año}) - {estado}")
    actual = actual.siguiente

# Menú principal
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar libro")
    print("2. Mostrar todos los libros")
    print("3. Buscar libro por título")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Eliminar libro")
    print("7. Ordenar por año")
    print("8. Ordenar por título")
    print("9. Estadísticas")
    print("10, Salir")

    opcion = input("\nOpción: ").strip()
    if opcion == "10":
        print("Hasta luego!")
        break
    elif opcion == "1":
        print("\n--- AGREGAR LIBRO ---")
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        año = int(input("Año: "))

        nuevo = Libro((titulo, autor, año, True))

        if inicio is None:
            inicio = nuevo
        else:
            actual = inicio
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        
        print(f"Libro '{titulo}' agregado con éxito ✅")
    
    elif opcion == "2":
        print("\n--- LIBROS ---")
        if inicio is None:
            print("No hay libros en la biblioteca")
        else:
            actual = inicio
            contador = 1
            while actual:
                titulo, autor, año, disponible = actual.datos
                estado = "Disponible" if disponible else "Prestado"
                print(f"{contador}. {titulo} - {autor} ({año}) - {estado}")
                actual = actual.siguiente
                contador += 1

    elif opcion == "3":
        print("\n--- BUSCAR LIBRO ---")
        buscar = input("Título a buscar: ").strip().lower()

        if inicio is None:
            print("No hay libros en la biblioteca")
        else:
            actual = inicio
            encontrado = False
            contador = 1
            while actual:
                titulo, autor, año, disponible = actual.datos
                if buscar in titulo.lower():
                    estado = "Disponible" if disponible else "Prestado"
                    print(f"Encontrado: {titulo} - {autor} ({año}) - {estado}")
                    encontrado = True
                actual = actual.siguiente
                contador += 1

            if not encontrado:
                print(f"No se encontró ningún libro con el título: {buscar}")

    elif opcion == "4":
        print("\n--- PRESTAR LIBRO ---")
        buscar = input("Título del libro: ").strip().lower()

        if inicio is None:
            print("No hay libros en la biblioteca")
        else:
            actual = inicio
            encontrado = False
            while actual:
                titulo, autor, año, disponible = actual.datos
                if buscar in titulo.lower():
                    encontrado = True
                    if disponible:
                        nuevo_datos = (titulo, autor, año, False)
                        actual.datos = nuevo_datos
                        print(f"Libro '{titulo}' prestado de manera exitosa")
                    else:
                        print(f"El libro '{titulo}' ya está prestado")
                    break
                actual = actual.siguiente

            if not encontrado:
                print(f"No se encontró ningún libro con título que contenga '{buscar}'")

    elif opcion == "5":
        print("\n--- DEVOLVER LIBRO ---")
        buscar = input("Título del libro a devolver: ").strip().lower()

        if inicio is None:
            print("No hay libros en la biblioteca")
        else:
            actual = inicio
            encontrado = False
            while actual:
                titulo, autor, año, disponible = actual.datos
                if buscar in titulo.lower():
                    encontrado = True
                    if not disponible:
                        nuevo_datos = (titulo, autor, año, True)
                        actual.datos = nuevo_datos
                        print(f"Libro '{titulo}' devuelto de manera exitosa")
                    else: 
                        print(f"El libro '{titulo}' estaba disponible")

                    break
                actual = actual.siguiente

            if not encontrado:
                print(f"No se encontró ningún libro con el título '{buscar}'")

    elif opcion == "6":
        print("\n--- ELIMINAR LIBRO ---")
        buscar = input("Título del libro que se va a eliminar: ").strip().lower()

        if inicio is None:
            print("No hay libros en la biblioteca")
        else:
            titulo, autor, año, disponible = inicio.datos
            if buscar in titulo.lower():
                inicio = inicio.siguiente
                print(f"Libro '{titulo}' eliminado exitosamente")
            else:
                actual = inicio
                while actual.siguiente is not None:
                    titulo_sig, autor_sig, año_sig, disponible_sig = actual.siguiente.datos
                    if buscar in titulo_sig.lower():
                        actual.siguiente = actual.siguiente.siguiente
                        print(f"Libro '{titulo_sig}' eliminado de manera exitosa")
                        break
                    actual = actual.siguiente
                else:
                    print(f"No se encontró ningún libro con el título '{buscar}'")
    
    elif opcion == "7":
        print("\n--- ORDENAR POR AÑO ---")
        if inicio is None or inicio.siguiente is None:
            print("Pocos libros para ordenar")
        else:
            inicio_ordenado = None
            actual = inicio

            while actual:
                titulo, autor, año, disponible = actual.datos
                nuevo = Libro((titulo, autor, año, disponible))

                if inicio_ordenado is None:
                    inicio_ordenado = nuevo
                else:
                    titulo0, autor0, año0, diponible0 = inicio_ordenado.datos
                    if año < año0:
                        nuevo.siguiente = inicio_ordenado
                        inicio_ordenado = nuevo
                    else:
                        actual_ord = inicio_ordenado
                        while actual_ord.siguiente is not None:
                            titulo_sig, autor_sig, año_sig, disponible_sig = actual_ord.siguiente.datos
                            if año < año_sig:
                                break
                            actual_ord = actual_ord.siguiente

                        nuevo.siguiente = actual_ord.siguiente
                        actual_ord.siguiente = nuevo

                actual = actual.siguiente

            inicio = inicio_ordenado
            print("Libros ordenados por año correctamente!")

    elif opcion == "8":
        print("\n--- ORDENAR POR TÍTULO (A-Z) ---")

        if inicio is None or inicio.siguiente is None:
            print("Pocos libros para ordenar")
        else:
            inicio_ordenado = None
            actual = inicio

            while actual:
                titulo, autor, año, disponible = actual.datos
                nuevo = Libro((titulo, autor, año, disponible))

                if inicio_ordenado is None:
                    inicio_ordenado = nuevo
                else:
                    titulo0, autor0, año0, disponible0 = inicio_ordenado.datos
                    if titulo.lower() < titulo0.lower():
                        nuevo.siguiente = inicio_ordenado
                        inicio_ordenado = nuevo
                    else:
                        actual_ord = inicio_ordenado
                        while actual_ord.siguiente is not None:
                            titulo_sig, autor_sig, año_sig, disponible_sig = actual_ord.siguiente.datos
                            if titulo.lower() < titulo_sig.lower():
                                break
                            actual_ord = actual_ord.siguiente

                        nuevo.siguiente = actual_ord.siguiente
                        actual_ord.siguiente = nuevo

                actual = actual.siguiente

            inicio = inicio_ordenado
            print("Libros ordenados por título correctamente")

    elif opcion == "9":
        print("\n--- ESTADÍSTICAS ---")
        if inicio is None:
            print("No hay libros en la biblioteca")
        else:
            total = 0
            disponibles = 0
            prestados = 0
            año_min = None
            año_max = None
            titulo_min = ""
            titulo_max = ""

            actual = inicio
            while actual:
                titulo, autor, año, disponible = actual.datos
                total += 1

                if disponible:
                    disponibles += 1
                else:
                    prestados += 1

                # Libro más antiguo
                if año_min is None or año < año_min:
                    año_min = año
                    titulo_min = titulo

                # Libro más reciente
                if año_max is None or año > año_max:
                    año_max = año
                    titulo_max = titulo

                actual = actual.siguiente

            print(f"Total libros: {total}")
            print(f"Libros disponibles: {disponibles}")
            print(f"Lisbros prestados: {prestados}")
            print(f"Libro más antiguo: {titulo_min} ({año_min})")
            print(f"Libro más reciente: {titulo_max} ({año_max})")