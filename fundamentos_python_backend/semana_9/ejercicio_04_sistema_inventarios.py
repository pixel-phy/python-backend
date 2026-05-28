"""Sistema de inventarios
Una tienda necesita gestionar su inventario con diccionarios. """

# Inventario: producto (precio, stock)

inventario = {
        "laptop": {"precio": 800, "stock": 10},
        "mouse": {"precio": 25, "stock": 50},
        "teclado": {"precio": 60, "stock": 20}
        }

while True:
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Mostrar inventario")
    print("2. Agregar producto")
    print("3. Vender producto")
    print("4. Ver stock bajo (menos de 5)")
    print("5. Acutalizar precio")
    print("6. Reponer stock")
    print("7. Valor de inventario")
    print("8. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        print("\n--- INVENTARIO ---")
        for producto, datos in inventario.items():
            print(f"{producto}: ${datos['precio']} - stock {datos['stock']}")


    elif opcion == "2":
        nombre = input("Nombre del producto: ")
        if nombre in inventario:
            print(f"'{nombre}' ya existe")
        else:
            precio = float(input("precio: "))
            stock = int(input("Stock inicial: "))
            inventario[nombre] = {"precio": precio, "stock": stock}
            print(f"'{nombre}' agregado")

    elif opcion == "3":
        nombre = input("Producto a vender: ")
        if nombre not in inventario:
            print(f"'{nombre}' no existe")
        else:
            cantidad = int(input("Cantidad: "))
            if cantidad > inventario[nombre]["stock"]:
                print(f"Stock insuficiente. Solo hay {inventario[nombre]['stock']}")
            else:
                inventario[nombre]["stock"] -= cantidad
                total = cantidad * inventario[nombre]["precio"]
                print(f"Venta realizada. Total: ${total}")
                print(f"Stock restante: {inventario[nombre]['stock']}")

    elif opcion == "4":
        print("\n--- STOCK BAJO (menos de 5) ---")
        hay_bajo = False
        for producto, datos in inventario.items():
            if datos["stock"] < 5:
                print(f"{producto}: {datos['stock']} unidades")
                hay_bajo = True
        if not hay_bajo:
            print("No hay productos con stock bajo")

    elif opcion == "5":
        print("\n--- ACTUALIZAR PRECIO ---")
        nombre = input("Producto a actualizar: ")
        if nombre not in inventario:
            print(f"'{nombre}' no existe")
        else:
            precio = float(input("Precio: "))
            inventario[nombre]["precio"] = precio
            print(f"Precio de '{nombre}' actualizado a ${precio}")

    elif opcion == "6":
        print("\n--- REPONER STOCK ---")
        nombre = input("Producto a reponer: ")
        if nombre not in inventario:
            print(f"'{nombre}' no existe")
        else:
            stock = int(input("Cantidad de stock: "))
            inventario[nombre]["stock"] += stock
            print(f"Stock '{nombre}' actualizado con éxito")
            print(f"Cantidad total {inventario[nombre]['stock']} unidades")

    elif opcion == "7":
        print("\n--- VALOR TOTAL DE INVENTARIO ---")
        valor_total = 0
        for producto, datos in inventario.items():
            print(f"{producto} - ${datos['precio']} ({datos['stock']} unidades)")
            valor_total += (datos['precio'] * datos['stock'])

        print(f"Valor total de inventario actual: ${valor_total}")

    elif opcion == "8":
        print("Hasta luego!")
        break

    else:
        print("Opción no válida")

