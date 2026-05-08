"""Lista de compras:
Se hace un programa simple de lista de compras.
1. Crear una lista vacía llamada compras.
2. Mostrar un menú que permita:
- Agregar artículo.
- Ver lista de compras.
- Eliminar el último artículo.
- Vaciar toda la lista.
- Salir del programa.
3. Validiar que no se pueda agregar un artículo vacío.
4. Mostrar mensajes amigables según la acción."""

print("\n=== LISTA DE COMPRAS ===\n")
compras = []

print("\n--- MENÚ PRINCIPAL ---\n")
print("1. Agregar artículo.")
print("2. Ver lista de compras.")
print("3. Eliminar el último artículo.")
print("4. Vaciar toda la lista.")
print("5. Salir del programa.")

while True:
    
    try:
        opcion = int(input("\nOpción: "))
        if opcion < 1 or opcion > 5:
            raise ValueError ("Escoja una opción válida (1-5)")
        elif opcion == 5:
            print("\nGracias por utilizar el programa. Hasta la próxima!")
            break
        elif opcion == 1:
            while True:
                articulo = input("Artículo: ").strip().lower()
                if articulo == "":
                    print("\nEl artículo no puede estar vacío.\n")
                    continue
                else:
                    compras.append(articulo)
                    print(f"\nEl artículo {articulo}, fue agregado a la lista de compras.")
                    break
        elif opcion == 2:
            if not compras:
                print("\nSin artículos en la lista.")
            else:
                print("\nLista de compras: ")
                for i, articulo in enumerate(compras, start=1):
                    print(f"{i}. {articulo}")
        elif opcion == 3:
            if not compras:
                print("\nLista de compras vacía. Ingrese algún artículo.")
            else:
                elim_articulo = compras.pop()
                print(f"\nSe ha eliminado {elim_articulo} de la lista de compras.\n")
        elif opcion == 4:
            if not compras:
                print("\nLista de compras vacía. Ingrese algún artículo.")
            else:
                compras.clear()
                print("\nArtículos eliminados de la lista de compras.")

    except ValueError as e:
        print(f"Error: {e}")
        continue