"""Proyecto integrador de pilas y colas:
Una clínica necesita un sistema para gestionar la atención de pacientes. Hay dos tipos de atención:
- Urgencias (prioridad alta): Se atiende primero
- Colsulta general (prioridad baja): Se atiende después
Dentro de cada tipo, se respeta el orden de llegada.
Requisitos:
1. Agregar paciente: nombre, tipo: urgencia/general (Dos colas separadas).
2. Atender paciente (primero urgencias, luego generales)
3. Mostrar colas en espera
4. Estadísticas: Total atendidos, urgencias atendidas, generales atendidas.
5. Salir."""

from collections import deque

urgencia = deque()
general = deque()
total_atendidos = 0
total_urgencias = 0
total_general = 0
total_espera = 0
espera_urgencias = 0
espera_general = 0

print("\n=== ATENCIÓN EN CLÍNICA ===")

while True:
    print("\n--- Menú principal ---")
    print("1. Agregar paciente")
    print("2. Atender paciente")
    print("3. Ver colas")
    print("4. Estadísticas")
    print("5. Salir")

    opcion = input("\nOpción: ")

    if opcion == "1":
        print("\n --- DATOS DEL PACIENTE ---")
        nombre = input("\nNombre: ").strip().title()
        if not nombre:
            print("Debe ingresar un nombre.")

        tipo = input("Tipo de atención (urgencia/general): ").strip().lower()
        if tipo == "urgencia":
            urgencia.append(nombre)
            print(f"Se agregó paciente a cola de 'urgencias'. Pacientes en cola {len(urgencia)}")
            espera_urgencias += 1
            
        else:
            general.append(nombre)
            print(f"Se agregó paciente a la cola 'general'. Pacientes en cola {len(general)}")
            espera_general += 1
        
        total_espera = espera_urgencias + espera_general        

    elif opcion == "2":
        if urgencia:
            print("\n--- Atendiendo pacientes de 'urgencia' ---")
            paciente_urgencia = urgencia.popleft()
            print(f"\nSe atendió a {paciente_urgencia}. Pacientes en cola: {len(urgencia)}")
            total_urgencias += 1
            espera_urgencias -= 1
        else:
            if general:
                print("\n--- Atendiendo pacientes de 'general' ---")
                paciente_general = general.popleft()
                print(f"\nSe atendió a {paciente_general}. Pacientes en cola: {len(general)}")
                total_general += 1
                espera_general -= 1
        
        total_atendidos = total_urgencias + total_general
        total_espera = espera_urgencias + espera_general

        if not urgencia and not general:
            print("Sin pacientes en colas")

    elif opcion == "3":
        print("\n--- PACIENTES EN COLA ---")
        if urgencia:
            print("Cola de 'urgencias': ")
            for i, paciente in enumerate(urgencia, 1):
                print(f"{i}. {paciente}")

        if general:
            print("\nCola 'general':")
            for i, paciente in enumerate(general, 1):
                print(f"{i}. {paciente}")

        if not urgencia and not general:
            print("\n Sin pacientes en cola para ser atendidos.")

    elif opcion == "4":
        print("\n --- ESTADÍSTICAS ---")
        print(f"\nTotal atendidos: {total_atendidos}")
        print(f"Urgencias: {total_urgencias}")
        print(f"General: {total_general}")
        print(f"\nTotal en espera: {total_espera}")
        print(f"Urgencias: {espera_urgencias}")
        print(f"General: {espera_general}")

    elif opcion == "5":
        print("Excelente turno. Hasta luego!")
        break
    else:
        print("Ingrese opción válida")