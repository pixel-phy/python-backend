"""Simulador de atención al cliente (pila vs cola)
Un sistema de atención al cliente quiere comparar dos modelos de atención:
- Cola(FIFO): El primero en llegar es el primero en ser atendido.
- Pila (LIFO): El último en llegar es el primero en ser atendido.
Requisitos:
- El problema debe permitir agregar clientes a una cola y a una pila (los mismos clientes en el mismo orden)
- Luego, atenderlos en ambos modelos y mostrar el orden de atención."""

from collections import deque

cola = deque()
pila = []

while True:
    print("\n--- Menú principal ---")
    print("1. Agregar cliente")
    print("2. Atender clientes")
    print("3. Salir")

    opcion = input("\nOpción: ")

    if opcion == "1":
        cliente = input("Cliente: ").strip().title()
        cola.append(cliente)
        pila.append(cliente)
    
    elif opcion == "2":
        print("\nOrden de llegada: ")
        for i, cliente in enumerate(pila, 1):
            print(f"{i}. {cliente}")
        print("\nOrden de atención en modelo cola: ")
        while cola:
            atendido = cola.popleft()
            print(f"Se atiende a: {atendido}")
        
        print("\nOrden de atención en modelo pila: ")
        while pila:
            atendido = pila.pop()
            print(f"Se atiende a: {atendido}")
        
    elif opcion == "3":
        print("Hasta luego!")
        break
    
    else:
        print("Opción inválida.")