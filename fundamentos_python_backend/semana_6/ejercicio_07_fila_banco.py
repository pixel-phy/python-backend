"""Fila de banco:
Simular una fila de atención al cliente donde el primero en llegar es el primero en ser atendido.
Menú:
1. Sacar turno (agregar cliente al final).
2. Atender cliente (al primero).
3. Ver fila de espera.
4. Salir."""

from collections import deque
fila = deque()

print("\n--- FILA EN UN BANCO ---")

while True:
    print("\n--- Menú ---")
    print("1. Sacar turno")
    print("2. Atender cliente")
    print("3. Ver fila de espera")
    print("4. Salir")

    opcion = input("\nOpción: ")

    if opcion == "1":
        nombre = input("\nNombre: ").strip().title()
        if nombre:
            fila.append(nombre)
            print(f"\n{nombre}. Su turno es {len(fila)}")
        else:
            print("Debe ingresar un nombre.")
            continue
    
    elif opcion == "2":
        if not fila:
            print("No hay nadie en la fila.")
        else:    
            atendido = fila.popleft()
            print(f"Pasa {atendido}")
            continue
        
    elif opcion == "3":
        if fila:
            print("Fila de espera: ")
            for i, nom in enumerate(fila, 1):
                print(f"{i}. {nom}")
            continue
        else:
            print("No hay nadie en la fila.")

    elif opcion == "4":
        print("Has salido.")
        break
    
    else:
        print("Ingrese una opción válida.")