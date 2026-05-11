"""historial de navegación:
Simular el botón "Atrás" de un navegador web.
"""
historial = []
pagina_actual = "Inicio"

while True:
    print(f"\nPágina actual: {pagina_actual}")
    print("\n--- Menú ---")
    print("1. Visitar nueva página")
    print("2. Atrás")
    print("3. Ver historial")
    print("4. Salir")

    opcion = input("\nOpción: ")

    if opcion == "1":
        nombre = input("URL: ").strip()
        if nombre:
            historial.append(pagina_actual)
            pagina_actual = nombre
            print(f"Ingresando a: {nombre}")
        else:
            print("No se puede visitar una página sin nombre.")

    elif opcion == "2":
        if historial:
            pagina_actual = historial.pop()
            print(f"Volviendo a: {pagina_actual}")
        else:
            print("No existe una página anteior.")
    
    elif opcion == "3":
        if historial:
            print("HISTORIAL: ")
            for i, pagina in enumerate(historial, 1):
                print(f"{i}. {pagina}")
        else: 
            print("Sin historial")

    elif opcion == "4":
        print("Hasta luego!")
        break

