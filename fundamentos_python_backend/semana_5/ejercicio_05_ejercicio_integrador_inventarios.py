"""Ejercicio integrador de inventarios
Sistema de inventarios simple (con listas paralelas).
productos = ["laptop", "mouse", "teclado", "monitor"]
precios = [800, 25, 60, 200]
stocks = [10, 50, 20, 5]

Operaciones: 
1. Mostrar inventario (producto - $precio - stock).
2. Calcular el valor del inventario.
3. Productos con stock < 10
4. Vender productos (pedir nombre y cantidad, validar stock).
5. Agregar producto nuevo."""

productos = ["laptop", "mouse", "teclado", "monitor"]
precios = [800, 25, 60, 200]
stocks = [10, 50, 20, 5]

while True:
    print("\n--- Menú Principal ---")
    print("1. Mostrar inventario")
    print("2. Calcular valor total del inventario")
    print("3. Productos con stock < 10")
    print("4. Vender producto")
    print("5. Agregar producto nuevo")
    print("6. Salir")
    
    try: 
        opcion = int(input("\nOpción: "))
        if opcion < 1 or opcion > 6:
            print("❌ Ingrese una opción válida.")
            continue

        #Mostrar inventario
        elif opcion == 1:
            print("\n--- INVENTARIO ---")
            for i in range(len(productos)):
                print(f"{productos[i]} - ${precios[i]} - {stocks[i]} u stock")
            continue

        # Valor total del inventario
        elif opcion == 2:
            suma = 0
            print("\n--- VALOR TOTAL ---")
            for i in range(len(precios)):
                suma += precios[i] * stocks[i]
            print(f"Suma total inventario: ${suma}")
            continue

        elif opcion == 3:
            # Stock < 10
            print("\n--- STOCK BAJO ---")
            for i in range(len(stocks)):
                if stocks[i] < 10:
                    print(f"{productos[i]} con {stocks[i]} u en stock")
            continue

        elif opcion == 4:
            print("\n--- Vender producto ---")
            while True:
                nombre = input("\nNombre: ").strip().lower()
                if not nombre: 
                    print("❌ Nombre no puede ir vacío.")
                    continue
                if nombre not in productos:
                    print("❌ Producto no disponible.")
                    continue
                break
            pos_producto = productos.index(nombre)
            while True:
                try:
                    cantidad = int(input("\nCantidad: "))
                    if cantidad < 0:
                        print("\n❌ Cantidad debe ser mayor que 0.")
                        continue
                    if cantidad > stocks[pos_producto]:
                        print(f"\nSólamente quedan {stocks[pos_producto]} en stock.")
                        continue
                    stocks[pos_producto] = stocks[pos_producto] - cantidad
                    print(f"\n✅ Se vendieron {cantidad} unidades de {productos[pos_producto]}. Quedan {stocks[pos_producto]} u en stock.")
                    total_venta = cantidad * precios[pos_producto]
                    print(f"Total venta: ${total_venta}")
                    break
                except ValueError:
                    print("\n❌ Ingrese una cantidad válida.")
                    continue
        # Agregar producto nuevo        
        elif opcion == 5:
            print("\n--- AGREGAR PRODUCTO ---")
            while True:
                nombre = input("Nombre: ").strip().lower()
                if not nombre:
                    print("\n❌ Debe ingresar un nombre.")
                    continue
                if nombre in productos:
                    print("❌ El producto ya existe.")
                    continue
                productos.append(nombre)
                break
            while True:
                try:
                    precio = float(input("Precio: "))
                    if precio < 0:
                        print("❌ El precio debe ser mayor que 0.")
                        continue
                    precios.append(precio)
                    break
                except ValueError:
                    print("❌ Ingrese un precio válido.")
                    continue
            while True:
                try:
                    cantidad = int(input("Cantidad: "))
                    if not cantidad:
                        print("❌ Ingrese una cantidad.")
                        continue
                    stocks.append(cantidad)
                    break
                except ValueError:
                    print("❌Ingrse una cantidad válida.")
                    continue
            print(f"✅ Se agregó {nombre} - ${precio} y {cantidad}u en stock")

        elif opcion == 6:
            print("Hasta luego!")
            break

    except ValueError:
        print("Ingrese una opción válida.")
        

    
    

    