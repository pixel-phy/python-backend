"""Simulador de fila en un banco:
- Agregar clientes a una cola
- Atender al primero (mostrar quién fue atendido)
- Mostrar cuántos quedan en cola."""

from collections import deque

cola = deque()

print("\n=== FILA DEL BANCO ===\n")

while True:
    print("1. Agregar cliente")
    print("2. Atender cliente")
    print("3. Ver fila")
    print("4. Salir")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        nombre = input("Nombre: ").strip().title()
        if nombre:
            cola.append(nombre)
            print(f"{nombre} agregado. Fila: {len(cola)}")
        else:
            print("Nombre no válido")
    
    elif opcion == "2":
        if cola:
            atendido = cola.popleft()
            print(f"Atendiendo a: {atendido}. Quedan {len(cola)}")
        else:
            print("No hay clientes en fila")
    
    elif opcion == "3":
        if cola:
            print(f"Clientes en fila ({len(cola)}):")
            for i, nombre in enumerate(cola, 1):
                print(f"  {i}. {nombre}")
        else:
            print("Fila vacía")
    
    elif opcion == "4":
        print("Hasta luego!")
        break
    
    else:
        print("❌ Opción no válida")