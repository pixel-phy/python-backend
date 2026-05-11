""" S1: Simular una pila:
Botón 'deshacer' en un editor de texto.
Cada vez que el usuario escribe algo, se apila. Cuando se oprime (Ctrl+Z) se deshace en orden. Al deshacer se desapila la última acción."""

historial = []
print("\n--- EDITOR DE TEXTO SIMULADO ---")
while True:
    print("\n1. Escribir texto")
    print("2. Deshacer (Ctrl + Z)")
    print("3. Ver historial")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        texto = input("Escriba el texto: ")
        historial.append(texto)
        print(f"'{texto}' agregado.")

    elif opcion == "2":
        if historial:
            deshecho = historial.pop()
            print(f"Deshecho: '{deshecho}'")
        else:
            print("No hay texto para deshacer.")
        
    elif opcion == "3":
        print(f"\nHistorial: {historial}")
    
    elif opcion == "4":
        print("Hasta luego!")
        break