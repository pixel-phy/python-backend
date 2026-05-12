"""Sistema de atención en un banco:
Un banco tiene dos tipos de clientes:
- Clientes preferenciales: (mayores de 60 años, descapacitados, mujeres embarazadas) --> prioridad alta.
- Clientes normales: prioridad baja
Los clientes preferenciales se atienden primero, y dentro de su misma categoría, por orden de llegada.

Datos por cliente:
- Nombre.
- Edad.
- Tipo (preferencia: edad >= 60 o si el usuario dice que tiene prioridad por motivo)

Requisitos:
1. Agregar cliente.
2. Atender cliente.
3. Ver colas.
4. Salir."""

from collections import deque

cola_preferencial = deque()
cola_normal = deque()

print("\n--- SISTEMA DE ATENCIÓN BANCARIO ---")

while True:
    print("\n--- Menú ---")
    print("1. Agregar cliente")
    print("2. Atender cliente")
    print("3. Ver colas")
    print("4. Salir")

    opcion = input("\nOpción: ")

    if opcion == "1":
        print("--- Agregar cliente ---")
        nombre = input("Nombre: ").strip().title()
        if not nombre:
            print("❌ Debe ingresar un nombre.")
            continue
        try:
            edad = int(input("Edad: "))
            if edad < 0 or edad > 120:
                print("La edad debe ser mayor que cero y menor que 120")
        except ValueError:
            print("❌ Ingrese un número válido.")
            continue
        es_preferencial = input("¿Es preferencial? (s/n): ")
        if es_preferencial == "s":
            tipo = input("Tipo: ").strip().lower()
            if tipo == "edad" and edad < 60:
                print("❌ La información no es coherente")
                continue
            cola_preferencial.append((nombre, edad))
            print(f"\n✅ Se agregó {nombre} de {edad} años (Cola preferencial)")
        else:
            cola_normal.append((nombre, edad))
            print(f"\n✅ Se agregó {nombre} de {edad} años (Cola normal)")

    elif opcion == "2":
        print("\n--- ATENDER CLIENTES ---")

        if not cola_preferencial and not cola_normal:
            print("❌ Sin clientes en ninguna de las filas.")

        else:
            if cola_preferencial:
                while cola_preferencial:
                    nombre, edad = cola_preferencial.popleft()
                    print(f"✅ Atendiendo a Preferencia: {nombre} {edad} años ({tipo}).")
            else:
                print("Sin clientes en cola preferencial.")
            
            if cola_normal:
                while cola_normal:
                    nombre, edad = cola_normal.popleft()
                    print(f"✅ Atendiendo a Normal: {nombre} {edad}.")
            else:
                print("Sin clientes en cola normal.")
            
    elif opcion == "3":
        print("\n--- INFORMACIÓN DE COLAS ---")
        if not cola_normal and not cola_preferencial:
            print("❌ Sin clientes en ninguna de las filas.")
        else:
            if cola_preferencial:
                print("\nCola preferencial: ")
                for i, (nombre, edad) in enumerate(cola_preferencial, 1):
                    texto = f"Preferencial: {tipo}"
                    print(f"{i}. Cliente: {nombre}, edad: {edad}, '{texto}'")
            else:
                print("Sin clientes en cola preferencial")
            
            if cola_normal:
                print("\nCola normal: ")
                for i, (nombre, edad) in enumerate(cola_normal, 1):
                    print(f"{i}. Cliente: {nombre}, edad: {edad}, 'No preferencial'.")
            else:
                print("Sin clientes en cola normal")

    elif opcion == "4":
        print("Hasta luego!")
        break

    else:
        print("Opción no válida")