"""Procesamiento por lotes con cola
Un sistema Backend recibe tareas (por ejemplo, envío de correos, generación de reportes, etc.)
y debe procesarlas en lotes de hasta 3 tareas por vez. Si hay más de 3, el resto queda esperando.

Requisitos:
- Usar una cola para las tareas.
- Cada tarea tiene: nombre y tiempo_estimado (segundos).
- Al procesar lote: tomar hasta 3 tareas de la cola y mostrarlas
- Simular el tiempo de procesamiento sumando los tiempos estimados
- Mostrar cuántas tareas quedan pendientes

Menú:
1. Agregar tarea
2. Procesar lote (máximo 3)
3. Ver tareas pendientes
4. Salir """

from collections import deque

cola = deque()

print("\n=== SISTEMA DE PROCESAMIENTO POR LOTES ===\n")

while True:
    print("\n--- Menú ---")
    print("1. Agregar tarea")
    print("2. Procesar lote (máx 3)")
    print("3. Ver tareas pendientes")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre de la tarea: ").strip()
        if not nombre:
            print("❌ La tarea debe tener un nombre.")
            continue
        
        try:
            tiempo = int(input("Tiempo estimado (segundos): "))
            if tiempo <= 0:
                print("❌ El tiempo debe ser mayor a 0.")
                continue
        except ValueError:
            print("❌ Ingrese un número válido.")
            continue
        
        cola.append((nombre, tiempo))
        print(f"✅ Tarea '{nombre}' agregada ({tiempo}s). Pendientes: {len(cola)}")

    elif opcion == "2":
        if not cola:
            print("❌ No hay tareas pendientes.")
            continue
        
        # Tomar hasta 3 tareas
        lotes = []
        for _ in range(min(3, len(cola))):
            lotes.append(cola.popleft())
        
        print(f"\n--- Procesando lote de {len(lotes)} tarea(s) ---")
        tiempo_total = 0
        for nombre, tiempo in lotes:
            print(f" {nombre} ({tiempo}s)")
            tiempo_total += tiempo
        
        print(f" Tiempo total estimado: {tiempo_total} segundos")
        print(f"✅ Lote procesado. Pendientes restantes: {len(cola)}")

    elif opcion == "3":
        if not cola:
            print("No hay tareas pendientes.")
        else:
            print(f"\n Tareas pendientes ({len(cola)}):")
            for i, (nombre, tiempo) in enumerate(cola, 1):
                print(f"  {i}. {nombre} ({tiempo}s)")

    elif opcion == "4":
        print("Hasta luego!")
        break

    else:
        print("❌ Opción no válida.")