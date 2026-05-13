"""Cola implementada con dos pilas:
En algunos sistemas, solo tienes pilas disponibles (por ejemplo, por restricciones del lenguaje o del entorono), 
pero necesitas el comportamiento FIFO de una cola. La solución es utilizar dos pilas.
Implementar una cola usando dos pilas con las siguientes operaciones:
1. Encolar.
2. Desencolar. 
3.  Ver frente.
4. Ver si está vacía.
5. Salir."""

print("\n--- COLA CON DOS PILAS ---")

pila_entrada = []
pila_salida = []

while True:
    print("\n--- Menú Principal ---")
    print("1. Encolar")
    print("2. Desencolar")
    print("3. Ver frente")
    print("4. Ver si está vacía")
    print("5. Salir")

    opcion = input("\nOpción: ")

    if opcion =="1":
        try:
            encolar = int(input("Valor: "))
            pila_entrada.append(encolar)
            print(f"✅ Encolado: {encolar}")
            
        except ValueError:
            print("Ingrese un número")

    elif opcion == "2":
        if not pila_salida:
            while pila_entrada:
                pila_salida.append(pila_entrada.pop())
        
        if pila_salida:
            desencolado = pila_salida.pop()
            print(f"✅ Desencolado: {desencolado}")
        else:
            print(f"❌ La cola está vacía. No hay elementos para desencolar.")
            
    elif opcion == "3":
        if not pila_salida:
            while pila_entrada:
                pila_salida.append(pila_entrada.pop())
        
        if pila_salida:
            print(f"Frente de la cola: {pila_salida[-1]}")
        else:
            print(f"La cola está vacía.")
        
    elif opcion == "4":
        if not pila_entrada and not pila_salida:
            print("La cola está vacía!")
        else:
            print(f"La cola no está vacía.")

    elif opcion == "5":
        print("Hasta luego!")
        break
    else:
        print("Ingrese una opción válida.")
