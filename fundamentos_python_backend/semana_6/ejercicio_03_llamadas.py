""" Sistema de atención telefónica:
Simular una pila de llamadas en espera.
Las llamadas se atienden en orden inverso (la última es la primera en atenderse)."""

llamadas = []
print(" \n--- SISTEMA DE ATENCIÓN TELEFÓNICA ---")

while True:
    print("1. Nueva llamada entrante")
    print("2. Atender llamada")
    print("3. Ver llamadas en espera")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        cliente = input("Nombre del cliente: ")
        llamadas.append(cliente)
        print(f"{cliente} cliente está en espera.")

    elif opcion == "2":
        if llamadas:
            atendiendo = llamadas.pop()
            print(f"Atendiendo a: {atendiendo}")
        else:
            print("No hay llamadas en espera")

    elif opcion == "3":
        print(f"En espera; {llamadas}")
    
    elif opcion == "4":
        print("Hasta luego!")
        break