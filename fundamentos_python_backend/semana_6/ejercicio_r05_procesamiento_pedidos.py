"""Procesamiento de pedidos en un sistema (COLA con dos pilas)
Trabajas en una empresa que tiene un sistema de procesamiento de pedidos muy antiguo.
El sistema solo permite usar pilas (LIFO) porque fue construido hace décadas y no se puede
cambiar. Pero necesitamos procesar pedidos en orde FIFO (El primero que llega es el primero
que se atiende). """

entrada = []
salida = []

while True:
    print("--- Menú principal ---")
    print("1. Entra pedido")
    print("2. Atender pedidos")
    print("3. Salir")

    opcion = input("\nOpción: ")

    if opcion == "1":

        pedido = input("Pedido: ").strip().title()

        if pedido:
            entrada.append(pedido)
            print(f"Se recibe pedido: {pedido}")
            continue
        else:
            print("El pedido no puede estar vacío")
            continue
    
    if opcion == "2":
        if not salida:
            while entrada:
                salida.append(entrada.pop())

        if salida:
            sale_pedido = salida.pop()
            print(f"Se prepara pedido:{sale_pedido} ")
            continue

        else:
            print("No se han agregado pedidos.")
    
    elif opcion == "3":
        print("Hasta luego!")
        break

    else:
        print("Ingrese una opción válida.")