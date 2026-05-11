"""Historial de navegación
Simular el botón 'Atrás' del navegador. Cada página nueva se apila. 'Atrás' desapila la última página."""

historial = []
pagina_actual = "Inicio"
print(f"Página actual: {pagina_actual}\n")

while True:
    print("1. Visitar nueva página")
    print("2. Atrás")
    print("3. Ver historial")
    print("4. Salir")

    opcion = input("Opcion: ")

    if opcion == "1":
        nueva = input("URL: ")
        historial.append(pagina_actual)
        pagina_actual = nueva
        print(f"✅ Visitando: {pagina_actual}")

    elif opcion == "2":
        if historial:
            pagina_actual = historial.pop()
            print(f"Volviendo a: {pagina_actual}")
        else:
            print("❌ No existe una página anterior.")
    
    elif opcion == "3":
        print(f"Historial: {historial}")
    
    elif opcion == "4":
        print("Hasta luego!")
        break