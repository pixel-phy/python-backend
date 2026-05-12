"""Simulación de procesos en una imprenta:
Una imprenta recibe trabajos de diferentes tipos. Los trabajos urgentes deben imprimirse antes que los normales, pero dentro de la misma prioridad,
se respeta el orden de llegada.
- Dos colas: cola_normal y cola_urgente
- Al agregar trabajo, preguntar si es urgente (s/n).
- Al imprimir, primero se imprimen todos los urgentes (en orden de llegada), luego los normales.
- Mostrar cola de espera. 
Datos:
- Nombre del trabajo.
- Número de páginas
- Urgente"""

from collections import deque

cola_normal = deque()
cola_urgente = deque()

while True:
    print("\n--- Menú ---")
    print("1. Agregar trabajo")
    print("2. Imprimir")
    print("3. Ver colas")
    print("4. Salir")

    opcion = input("\nOpción: ")

    if opcion == "1":
        nombre = input("Nombre del trabajo: ").strip()
        if not nombre:
            print("❌ El nombre no puede estar vacío.")
            continue
        
        try:
            paginas = int(input("Número de páginas: "))
            if paginas < 1:
                print("❌ Mínimo 1 página.")
                continue
        except ValueError:
            print("❌ Ingrese un número válido.")
            continue
        
        urgente = input("¿Es urgente? (s/n): ").strip().lower()

        if urgente == "s":
            cola_urgente.append((nombre, paginas))
            print(f"✅ Trabajo urgente {nombre} agregado a cola.")
        else:
            cola_normal.append((nombre, paginas))
            print(f"✅ Trabajo normal {nombre} agregado a cola.")

    elif opcion == "2":
        print("\n--- IMPRIMIENDO ---")

        while cola_urgente:
            nombre, paginas = cola_urgente.popleft()
            print(f"Imprimiendo (urgente) {nombre} ({paginas} páginas)")

        while cola_normal:
            nombre, paginas = cola_normal.popleft()
            print(f"Imprimiendo (normal) {nombre} ({paginas} páginas)")
        
    elif opcion == "3":
        print("\n--- COLA URGENTE ---")
        if cola_urgente:
            for i, (nombre, paginas) in enumerate(cola_urgente, 1):
                print(f"{i}. {nombre} - {paginas} páginas")

        else:
            print("Cola vacía")
        
        print("\n--- COLA NORMAL ---")
        if cola_normal:
            for i, (nombre, paginas) in enumerate(cola_normal, 1):
                print(f"{i}. {nombre} - {paginas} páginas")
        
        else:
            print("Cola vacía.")
    
    elif opcion == "4":
        print("Hasta luego!")
        break

    else:
        print("❌ Ingrese una opción válida.")