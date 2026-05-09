"""Lista de compras mejorado
Un programa que permita gestionar una lista de compras con las siguientes operaciones:
1. Agregar artículo (sin duplicados).
2. Ver lista de compras.
3. Marcar artículo como comprado (lo elimina de la lista de pendientes y lo pasa a una lista de "comprados").
4. Ver artículos comprados.
5. Vaciar lista de pendientes.
6. salir.

Requisitos:
- Dos listas: pendientes y comprados.
- Validar que no se agreguen artículos vacíos. 
- Validar que no se agreguen duplicados en pendientes.
- Al marcar como comprado, mover el artículo de pendientes a comprados."""

print("\n--- LISTA DE COMPRAS ---\n")
comprados = []
pendientes = []

while True:
    print("\n--- Menú principal ---")
    print("1. Agregar artículo.")
    print("2. Ver lista de compras.")
    print("3. Marcar artículo comprado.")
    print("4. Ver artículos comprados.")
    print("5. Vaciar lista de pendientes.")
    print("6. Salir.")
    try:
        opcion = int(input("\nOpción: "))
        if opcion < 1 or opcion > 6:
            print("❌ Señale una opción entre (1-6).\n")
            continue

        elif opcion == 1:
            while True:
                articulo = input("Nombre artículo: ").strip().lower()
                if not articulo:
                    print("❌El nombre del artículo no puede estar vacío.")
                    continue

                if articulo in pendientes:
                    print(f"❌ '{articulo}' ya está en la lista de pendientes.")
                    continue
                
                pendientes.append(articulo)
                print(f"✅ El artículo '{articulo}' se agregó a la lista de pendientes.")
                break
        
        elif opcion == 2:
            if not pendientes:
                print("❌ Lista de compras vacía.")
                continue
            print("\nLista de compras pendientes: ")
            for i in pendientes:
                print(f"- {i}")

        elif opcion == 3:
            if not pendientes:
                print("❌ No tiene artículos pendientes por comprar.")
                continue
            print("\nArtículos por comprar pendientes:")
            for i, art in enumerate(pendientes):
                print(f"{i+1} - {art}")
            while True:
                art_comprado = input("\nIngrese el número del artículo que compró: ")
                if not art_comprado:
                        print("❌ El artículo comprado no puede estar vacío.")
                        continue
                try:
                    articulo_comprado = int(art_comprado)

                    if articulo_comprado < 1 or articulo_comprado > len(pendientes):
                        print(f"❌ El número debe estar entre 1 y {len(pendientes)}")
                        continue
                    
                    agregar_articulo_comprado = pendientes[articulo_comprado - 1]
                    comprados.append(agregar_articulo_comprado)
                    pendientes.pop(articulo_comprado - 1)
                    print(f"\n✅Se agregó '{agregar_articulo_comprado}' a la lista de comprados")
                    break

                except ValueError:
                    print("❌ Ingrese un número válido!")
                    continue

        elif opcion == 4:
                if not comprados:
                    print("❌ La lista de comprados está vacía.")
                    continue
                print("\nLista de comprados: ")
                for i, art in enumerate(comprados):
                    print(f"{i+1}. {art.upper()}")

        elif opcion == 5:
            if not pendientes:
                print("La lista de pendientes está vacía.")
                continue

            pendientes.clear()
            print("✅ Se ha vaciado la lista de artículos pendientes por comprar.")
            continue

        elif opcion == 6:
            print("Hasta la próxima!")
            break

    except ValueError:
        print("❌ Opción no válida!")
        continue