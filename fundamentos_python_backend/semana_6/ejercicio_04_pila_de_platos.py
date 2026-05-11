"""Pila de platos:
En una cocina, los platos se lavan y se apilan. El último plato lavado es el primero en usarse.

Requisitos:
- Se debe mostrar un menú con opciones:
1. Lavar un plato (apilar).
2. Usar plato (desapilar).
3. Ver pila de platos.
4. Salir.
- Al lavar un plato, se pide el nombre del plato y se agrega a la pila. 
- Al usar un plato, se toma el último de la pila y se muestra cuál fue.
- No se puede usar un plato si no hay platos en la pila. 
- No se puede lavar un plato sin nombre."""

platos = []

print("\n--- PILA DE PLATOS ---")

while True:
    print("\n--- Menú principal ---")
    print("1. Lavar un plato")
    print("2. Usar plato")
    print("3. Ver pila de platos")
    print("4. Salir")

    opcion = input("\nOpción: ")

    if opcion == "1":
        nombre = input("Nombre: ").strip()
        if nombre:
            platos.append(nombre)
            print(f"✅ {nombre} apilado.")
        else:
            print("❌ No es posible apilar")
    
    elif opcion == "2":
        if platos:   
            usado = platos.pop()
            print(f"✅ Se usa {usado}. Quedan {len(platos)} platos.")
        else:
            print("❌ No hay platos apilados.")

    elif opcion == "3":
        if platos:
            print("Platos apilados: ")
            for i, plato in enumerate(reversed(platos), 1):
                print(f" {i}. {plato}")
        else:
            print("❌ No hay platos apilados")
    
    elif opcion == "4":
        print("Hasta luego!")
        break
    