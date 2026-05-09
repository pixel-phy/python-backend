"""Sistema de inventario simple
Una tienda maneja productos con tres listas paralelas:
productos, precios, stocks.
productos = ["laptop", "mouse", "teclado"]
precios = [800, 25, 60]
stocks = [10, 50, 20]
Requisitos:
ver inventario:
1. producto - $precio (stock).
2. Agregar producto - Pedir nombre, precio, stock y agregar a las tres listas.
3. Vender producto - Pedir nombre y cantidad, verificar que exista y que haya stock suficiente, luego restar stock.
4. Productos con bajo stock - mostrar productos con stock < 5.
5. Valor total del inventario - Sumar precio * stock de todos los productos. 
6. Salir."""

print("\n=== SISTEMA DE INVENTARIO ===\n")
productos = ["laptop", "mouse", "teclado"]
precios = [800, 25, 60]
stocks = [10, 50, 20]

while True:
    print("\n--- Menú principal ---")
    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Vender producto")
    print("4. Productos con bajo stock (<5)")
    print("5. Valor total del inventario")
    print("6. Salir")
    
    try:
        opcion = int(input("\nOpción: "))
        
        if opcion == 1:
            print("\n--- Inventario ---")
            for i, p in enumerate(productos):
                print(f"{i+1}. {p} - ${precios[i]} (stock {stocks[i]})")
        
        elif opcion == 2:
            nombre = input("Nombre: ").strip().lower()
            if not nombre:
                print("❌ El nombre no puede estar vacío")
                continue
            
            try:
                precio = float(input("Precio: "))
                if precio <= 0:
                    print("❌ El precio debe ser mayor a 0")
                    continue
                stock = int(input("Stock: "))
                if stock < 0:
                    print("❌ El stock no puede ser negativo")
                    continue
            except ValueError:
                print("❌ Ingrese valores numéricos válidos")
                continue
            
            productos.append(nombre)
            precios.append(precio)
            stocks.append(stock)
            print(f"✅ Producto '{nombre}' agregado (${precio}, stock {stock})")
        
        elif opcion == 3:
            nombre = input("Nombre del producto: ").strip().lower()
            if not nombre:
                print("❌ El nombre no puede estar vacío")
                continue
            
            if nombre not in productos:
                print(f"❌ '{nombre}' no existe en el inventario")
                continue
            
            try:
                cantidad = int(input("Cantidad a vender: "))
                if cantidad <= 0:
                    print("❌ La cantidad debe ser mayor a 0")
                    continue
            except ValueError:
                print("❌ Ingrese un número válido")
                continue
            
            indice = productos.index(nombre)
            if cantidad > stocks[indice]:
                print(f"❌ Stock insuficiente. Solo hay {stocks[indice]} unidades")
                continue
            
            stocks[indice] -= cantidad
            print(f"✅ Venta realizada. Stock actual de '{nombre}': {stocks[indice]}")
        
        elif opcion == 4:
            print("\n--- Productos con bajo stock (<5) ---")
            hay_bajo = False
            for i in range(len(productos)):
                if stocks[i] < 5:
                    print(f"{productos[i]}: {stocks[i]} unidades")
                    hay_bajo = True
            if not hay_bajo:
                print("No hay productos con stock bajo")
        
        elif opcion == 5:
            total = 0
            for i in range(len(productos)):
                total += precios[i] * stocks[i]
            print(f"\nValor total del inventario: ${total}")
        
        elif opcion == 6:
            print("¡Hasta luego!")
            break
        
        else:
            print("❌ Opción no válida (1-6)")
    
    except ValueError:
        print("❌ Ingrese un número válido")