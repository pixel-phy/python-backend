"""Sistema de inventario simple
Una tienda necesita gestionar su inventario de productos: ver productos, agregar, eliminar y actualizar precios.

- Usar listas para productos y precios.
- Mostrar menú:
1. Ver inventario.
2. Agregar producto.
3. Eliminar producto.
4. Actualizar precio.
5. Salir.

Detalles:
1. Ver inventario: mostar lista enumerada comenzando en 1, con formato "1. manzana - $100"
2. Agregar producto: pedir nombre y precio, agregar a ambas listas.
3. Eliminar producto: mostrar inventario y pedir número (índice), eliminar de ambas listas.
4. Actualizar precio: mostrar inventario, pedir número y nuevo precio.
5. Salir: terminar programa."""

print("\n=== SISTEMA DE INVENTARIO ===\n")
productos = ["manzana", "pera", "uva"]
precios = [100, 200, 150]

while True:
    print("\n--- Menú principal ---\n")
    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Actualizar precio")
    print("5. Salir")
    try:
        opcion = int(input("\nOpción: "))
        if opcion < 1 or opcion > 5:
            print("\nSelecciona una opción válida (1 - 5)\n")
            continue

        elif opcion == 1:
            print("\n--- INVENTARIO ---\n")
            for i in range(len(productos)):
                print(f"{i+1}. {productos[i]} - ${precios[i]}")
        
        elif opcion == 2:
            while True:
                nombre = input("\nNombre: ").strip().lower()

                if nombre:
                    productos.append(nombre)
                    break
                else:
                    print("\nEl nombre del producto no puede estar vacío.\n")
                    continue
            
            while True:
                try:
                    precio = float(input(f"\nPrecio ({nombre}): "))
                    if precio < 0:
                        print("\nEl precio no debe ser menor que 0.\n")
                        continue
                    elif precio:
                        precios.append(precio)
                        print(f"\nSe agregó {productos[-1]} con precio ${precios[-1]}\n")
                        break

                except ValueError:
                    print("\nEl precio debe ser un número.\n")
                    continue

        elif opcion == 3:
            print("\n --- INVENTARIO ---\n")
            print("\nÍndice | Producto")
            for i, producto in enumerate(productos):
                print(f"{i}     | {producto.capitalize()}")
            
            while True:
                try:
                    eliminar = int(input("Índice del producto a eliminar: "))
                    if eliminar < 0 or eliminar >= len(productos):
                        print(f"\nEl índice no debe ser menor que 0 ni mayor que {len(productos) - 1}\n")
                        continue
                    else:
                        producto_eliminado = productos.pop(eliminar)
                        precio_eliminado = precios.pop(eliminar)
                        print(f"\n Se eliminó {producto_eliminado} con precio: ${precio_eliminado}\n")
                        break

                except ValueError:
                    print("\nIngrese un índice válido.")
                    continue

        elif opcion == 4:
            print("\n --- INVENTARIO --- \n")
            print("\nÍndice | Producto")
            for i, producto in enumerate(productos):
                print(f"{i}     | {producto.capitalize()}")

            while True:
                try:
                    modificar = int(input("\nÍndice del producto: "))
                    if modificar < 0 or modificar >= len(productos):
                        print(f"\nEl índice no debe ser menor que 0 ni mayor que {len(productos) - 1}\n")
                        continue
                    else:
                        precio_modificado = precios[modificar]
                        producto_modificado = productos[modificar]
                        print(f"\nSe modificará a {producto_modificado} con ${precio_modificado}.\n ")
                        break
                except ValueError:
                    print("\nIngrese un índice válido.\n")
                    continue

            while True:
                try:
                    valor = float(input("\nPrecio nuevo: "))
                    if valor < 0:
                        print("\nEl precio debe ser mayor que 0\n")
                        continue
                    else:
                        precios[modificar] = valor

                        break
                except ValueError:
                    print("\nIngrese un valor válido.\n")
                    continue

        elif opcion == 5:
            print("\nGracias por usar el sistema de inventarios!\n")
            break
                    
    except ValueError:
        print("\nOpción inválida.\n")
        continue