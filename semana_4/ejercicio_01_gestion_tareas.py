"""Gestión de tareas:
Un sistema de tareas pendiente.
Requisitos:
1. Crear lista vacía tareas = []
2. Mostrar menú:
- Agregar tarea.
- Eliminar tarea.
- Mostrar todas.
- Salir.
3. Agregar: pedir descripción y usar .append().
4. Eliminar: mostrar índice de cada tarea y eliminar por índice.
5. Mostrar: recorrer la lista y mostrar elementos."""

print("\n=== GESTIÓN DE TAREAS ===\n")
tareas = []
while True:
    print("\n--- Menú ---\n")
    print("1. Agregar tarea.")
    print("2. Eliminar tarea.")
    print("3. Mostrar todas.")
    print("4. Salir")
    entrada = input("\nOpción: ").strip()
    try:
        opcion = int(entrada)
        if opcion < 1 or opcion > 4:
            print("\n❌ Ingrese una de las opciones (1-4) \n")
            continue
        elif opcion == 1:
            tarea = input("Tarea: ").strip()
            tareas.append(tarea)
            print("\n✅ Tarea agregada con éxito!\n")
            continue
        elif opcion == 2:
            if not tareas:
                print("\n❌ Sin tareas disponibles para eliminar.")
                continue
            else:
                print("\nÍndice | Tarea")
                for index, l in enumerate(tareas):
                    print(f"{index}     |   {l}")
                
                while True:
                    entrada_eliminar = input("\nÍndice de la tarea a eliminar: ")
                    try:
                        eliminar = int(entrada_eliminar)
                        if eliminar < 0 or eliminar >= len(tareas):
                            print(f"\n❌ Índice fuera de rango.")
                            continue
                        else:
                            tareas.pop(eliminar)
                            print("\n✅ Tarea eliminada.")
                            break
                    except ValueError:
                        print("Ingrese un elemento válido.")
                        continue
        elif opcion == 3:
            if not tareas:
                print("❌ Sin tareas para mostrar.")
                continue
            else:
                print(f"Tareas: {tareas}")
                continue
        elif opcion == 4:
            print("Saliste del programa. Gracias por usar la APP.")
            break
        else:
            print("❌ Ingrese una de las opciones del menú.")
            continue        
    except ValueError:
        print("❌ Ingrese una opción válida.")