"""Simular una cola de impresión:
Una impresora recibe documentos y los imprime en orden de llegada."""

from collections import deque

nombres = deque()   
paginas = deque()  

print("\n=== COLA DE IMPRESIÓN ===\n")

while True:
    print("\n--- Menú ---")
    print("1. Agregar documento")
    print("2. Imprimir documento")
    print("3. Ver cola de impresión")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre del documento: ").strip().title()
        if not nombre:
            print(" El nombre no puede estar vacío.")
            continue
        
        try:
            cant_paginas = int(input("Número de páginas: "))
            if cant_paginas <= 0:
                print(" El documento debe tener al menos 1 página.")
                continue
        except ValueError:
            print(" Ingrese un número válido.")
            continue
        
        nombres.append(nombre)
        paginas.append(cant_paginas)
        print(f" '{nombre}' agregado ({cant_paginas} páginas). Posición en cola: {len(nombres)}")

    elif opcion == "2":
        if nombres and paginas:
            nombre_actual = nombres.popleft()
            paginas_actual = paginas.popleft()
            
            print(f" Imprimiendo '{nombre_actual}'... ({paginas_actual} páginas)")

            print(f" '{nombre_actual}' impreso.")
        else:
            print(" No hay documentos en la cola.")

    elif opcion == "3":
        if nombres and paginas:
            print("\n Cola de impresión:")
            for i in range(len(nombres)):
                print(f"  {i+1}. '{nombres[i]}' - {paginas[i]} páginas")
        else:
            print(" No hay documentos en cola.")

    elif opcion == "4":
        print(" ¡Hasta luego!")
        break

    else:
        print(" Opción no válida.")