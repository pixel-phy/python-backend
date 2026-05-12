"""Cola de pedidos de resetaurante:
Un restaurante recibe pedidos y los procesa en orden de llegada. Cada pedido tiene:

- Nombre del cliente.
- Plato principal.
- Si es para llevar (True/False)

Requisitos:
- Usar deque donde cada elemento es una tupla (cliente, plato, para_llevar).
- Al agregar pedido: pedir los datos
- Al procesar pedido: mostrar mensaje según si es para llevar o no
- Mostrar cola de pedidos pendientes """

from collections import deque

pedido = deque()

while True:
    print("\n--- Menú --- ")
    print("1. Agregar pedido")
    print("2. Procesar pedidos")
    print("3. Mostrar pedidos pendientes")
    print("4. Salir")

    opcion = input("\nOpción: ")

    if opcion == "1":
        print("\n--- Pedido nuevo ---")

        cliente = input("Cliente: ").strip().title()
        if not cliente:
            print("❌ El cliente no puede ir vacío")
            continue

        plato = input("Plato: ").strip().title()
        if not plato:
            print("❌ El plato no puede ir vacío")
            continue

        para_llevar = input("¿Para llevar? (s/n): ").strip().lower()
        if para_llevar == "s":
            pedido.append((cliente, plato, True))
            print(f"✅ Pedido de {cliente} agregado (para llevar)")
            
        else:
            pedido.append((cliente, plato, False))
            print(f"✅ Pedido agregado {cliente} agregado (para comer aquí)")
            
    elif opcion == "2":
        print("\n--- Procesando pedidos ---")

        if not pedido:
            print("Sin pedidos para procesar")

        while pedido:
            cliente, plato, para_llevar = pedido.popleft()
            if para_llevar:
                print(f"{cliente} pidió {plato} (Para llevar)")
            else:
                print(f"{cliente} pidió {plato} (Para comer aquí)")
        
        print("✅ Todos los pedidos se procesaron!")
        
    elif opcion == "3":
        print("\n--- PEDIDOS ---")
        if pedido:
            for i, (cliente, plato, para_llevar) in enumerate(pedido, 1):
                texto = "Para llevar" if para_llevar else "Comer aquí"
                print(f"{i}. {cliente}: {plato} ({texto})")
        else:
            print("Sin pedidos en pendientes")

    elif opcion == "4":
        print("Hasta luego!")
        break

    else:
        print("❌ Ingrese una opción válida!")        