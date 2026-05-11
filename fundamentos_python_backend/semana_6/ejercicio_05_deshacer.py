"""Deshacer:
Editor de texto con deshacer.
texto_actual = "" 
historial = []
Menú:
1. Escribir.
2. Deshacer.
3. Ver historial.
4. Salir.

- Al escribir, guardar el estado actual en historial antes de modificar.
- Al deshacer, recuperar el último estado guardado (si existe).
- No se puede deshacer si historial está vacío."""

print("\nEDITOR DE TEXTO")
texto_actual = ""
historial = []

while True:
    print(f"\nTexto actual: {texto_actual}")
    print("\n--- Menú ---")
    print("1. Escribir")
    print("2. Deshacer")
    print("3. Ver historial")
    print("4. Salir")

    opcion = input("\nOpción: ").strip()

    if opcion == "1":

        texto = input("Escribir: ")

        if texto:
            historial.append(texto_actual)
            if texto_actual:
                texto_actual += " " + texto
            else:
                texto_actual = texto
        else: 
            print("No se agrega texto vacío.")
    
    elif opcion == "2":
        if historial:
            texto_actual = historial.pop()
            print ("Deshecho")
        else:
            print("Nada que deshacer.")
        
    elif opcion == "3":
        if historial:
            print("Historial: ")
            for i, estado in enumerate(historial, 1):
                print(f"{i}. {estado}")
        else:
            print("Historial vacío.")

    elif opcion == "4":
        print("Hasta luego!")
        break
    
    else:
        print("❌ Opción no válida.")
