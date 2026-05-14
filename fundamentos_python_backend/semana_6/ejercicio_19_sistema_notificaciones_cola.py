"""Sistema de notificaciones con cola
Un sistema backend debe enviar notificaciones a usuaios (correos, push, SMS). Las notificaciones se encolan y se envían 
en orden de llegada, pero con un límite de 2 notificaciones por segundo (simulado).

Requisitos:
1. Agregar notificaciones.
2. Enviar notificaciones (una a una, con límite de 2 por segundo)
3. Ver cola pendiente.
4. Salir. (mostrar estadísticas)"""

from collections import deque

cola = deque()
enviadas = 0
enviadas_email = 0
enviadas_push = 0
enviadas_sms = 0

print("\n=== SISTEMA DE NOTIFICACIONES ===\n")

while True:
    print("\n--- Menú principal ---")
    print("1. Agregar notificación")
    print("2. Enviar notificaciones (máx 2)")
    print("3. Ver cola pendiente")
    print("4. Salir (mostrar estadísticas)")

    opcion = input("Opción: ")

    if opcion == "1":
        usuario = input("Usuario: ").strip()
        if not usuario:
            print("El usuario no puede estar vacío.")
            continue
        
        mensaje = input("Mensaje: ").strip()
        if not mensaje:
            print("El mensaje no puede estar vacío.")
            continue
        
        tipo = input("Tipo (email/push/sms): ").strip().lower()
        if tipo not in ["email", "push", "sms"]:
            print("Tipo no válido. Use email, push o sms.")
            continue
        
        cola.append((usuario, mensaje, tipo))
        print(f"Notificación agregada para {usuario}. Pendientes: {len(cola)}")

    elif opcion == "2":
        if not cola:
            print("No hay notificaciones pendientes.")
            continue
        
        enviar_hoy = []
        for _ in range(min(2, len(cola))):
            enviar_hoy.append(cola.popleft())
        
        print(f"\n--- Enviando {len(enviar_hoy)} notificación(es) ---")
        
        for usuario, mensaje, tipo in enviar_hoy:
            print(f"Enviando {tipo} a {usuario}: {mensaje}")
            enviadas += 1
            
            if tipo == "email":
                enviadas_email += 1
            elif tipo == "push":
                enviadas_push += 1
            elif tipo == "sms":
                enviadas_sms += 1
        
        print(f"✅ Procesadas. Pendientes restantes: {len(cola)}")

    elif opcion == "3":
        if not cola:
            print("No hay notificaciones pendientes.")
        else:
            print(f"\nNotificaciones pendientes ({len(cola)}):")
            for i, (usuario, mensaje, tipo) in enumerate(cola, 1):
                print(f"  {i}. {tipo} para {usuario}: {mensaje}")

    elif opcion == "4":
        print("\n--- ESTADÍSTICAS FINALES ---")
        print(f"Total notificaciones enviadas: {enviadas}")
        print(f"  email: {enviadas_email}")
        print(f"  push: {enviadas_push}")
        print(f"  sms: {enviadas_sms}")
        print("Hasta luego!")
        break

    else:
        print("❌ Opción no válida.")