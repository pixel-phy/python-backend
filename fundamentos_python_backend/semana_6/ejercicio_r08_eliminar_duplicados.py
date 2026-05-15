"""Eliminar duplicados (manteniendo orden)
Una lista tiene elementos repetidos. Quieres quedarte solo con la primera aparición de cada uno,
respectando el orden original."""

lista = []

while True:
    print("\n--- Menú ---")
    print("1. Agregar elemento")
    print("2. Mostrar lista completa")
    print("3. Mostrar lista sin repetidos")
    print("4. Salir")

    opcion = input("\nOpción: ")

    if opcion == "1":
        elemento = input("\nElemento: ").strip().lower()
        if elemento:
            lista.append(elemento)
            continue
        else:
            print("La palabra no puede estar vacía")
            continue

    elif opcion == "2":
        if not lista:
            print("No hay elementos para mostrar.")
            continue
        else:
            print("\nElementos en lista:")
            for i, elem in enumerate(lista):
                print(f"{i}. {elem}")
            continue

    elif opcion == "3":
        if not lista:
            print("No hay elementos para mostrar")
            continue
        else:
            un_solo_elemento = []
            print("\nLista sin repetidos:")
            for elem in lista:
                if elem not in un_solo_elemento:
                    un_solo_elemento.append(elem)
            for i, elem in enumerate(un_solo_elemento):
                print(f"{i}. {elem}")

    elif opcion == "4":
        print("Hasta luego!")
        break
    else:
        print("Opción no válida")