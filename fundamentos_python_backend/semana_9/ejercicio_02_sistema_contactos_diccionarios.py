"""Sistema de contactos con diccionarios:
    Una agenda telefónica usando diccionarios."""

#Agenda: nombre: (teléfono, email)
agenda = {
        "Ana": {"telefono": "123456789", "email": "ana@mail.com"},
        "Luis": {"telefono": "987654321", "email": "luis@mail.com"},
        "Carlos": {"telefono": "5555555555", "email": "carlos@mail.com"}
        }
while True:
    print("\n--- Agenda de contactos ---")
    print("1. Mostrar todos los contactos")
    print("2. Buscar contacto")
    print("3. Agregar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        print("\n=== CONTACTOS ===")
        for nombre, datos in agenda.items():
            print(f"{nombre}: {datos['telefono']} - {datos['email']}")

    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        if nombre in agenda:
            datos = agenda[nombre]
            print(f"{nombre}: {datos['telefono']} - {datos['email']}")
        else:
            print(f"'{nombre}' no encontrado")

    elif opcion == "3":
        nombre = input("Nombre: ")
        if nombre in agenda:
            print(f"'{nombre}' ya existe")
        else:
            telefono = input("Teléfono: ")
            if telefono.isdigit() and len(telefono) >= 7:
                email = input("Email: ")
                if '@' in email and "." in email:
                    agenda[nombre] = {"telefono": telefono, "email": email}
                    print(f"'{nombre}' agregado")
                else:
                    print("Email inválido (debe contener @ y .)")
            else:
                print("Teléfono inválido (debe tener al menos 7 dígitos)")

    elif opcion == "4":
        nombre = input("Nombre a eliminar: ")
        if nombre in agenda:
            del agenda[nombre]
            print(f"'{nombre}' eliminado")
        else:
            print(f"'{nombre}' no encontrado")

    elif opcion == "5":
        print("Hasta luego!")
        break

    else:
        print("Opción no válida")
