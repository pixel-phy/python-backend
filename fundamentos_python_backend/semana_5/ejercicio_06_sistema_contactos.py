"""Sistema de contactos:
Una agenda telefónica simple para gestionar contactos usando listas paralelas.
nombres = ["Ana", "Luis", "Carlos"]
telefonos = ["123456789", "987654321", "555555555"]
emails = ["ana@mail.com", "luis@mail.com", "carlos@mail.com"]

1. Mostrar todos los contactos: 1. nombre - telefóno - correo.
2. Agregar contacto.
- Pedir nombre, teléfono y email.
- Validar que el nombre no esté vacío.
- Validar que el teléfono tenga al menos 7 dígitos (sólo números)
- Validar que el email contenga @ y .
- Agregar a las tres listas.
3. Buscar contacto
- Buscar por nombre (búsqueda parcial, sin distinción de mayúsculas)
- Mostrar todos los resultados encontrados.
4. Eliminar contacto
- Mostrar lista numerada de contactos.
- Pedir el número del contacto a eliminar.
- Eliminar de las tres listas en el mismo índice.
5. Menú principal.
"""

nombres = ["Ana", "Luis", "Carlos"]
telefonos = ["123456789", "987654321", "555555555"]
emails = ["ana@mail.com", "luis@mail.com", "carlos@mail.com"]

while True:
    print("\n---MENÚ PRINCIPAL ---")
    print("1. Mostrar contactos")
    print("2. Agregar contacto")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    
    try:
        opcion = int(input("\nOpción: "))
        if opcion < 1 or opcion > 6:
            print("❌ Opción no válida.")
            continue
        # Mostrar contactos
        elif opcion == 1:
            print("\n--- CONTACTOS ---")
            for i, nombre in enumerate(nombres):
                print(f"{i+1}. {nombres[i]} - {telefonos[i]} - {emails[i]}")
            continue
        
        # Agregar contacto
        elif opcion == 2:
            print("\n--- AGREGAR CONTACTO ---")
            while True:
                nombre = input("Nombre: ").strip().lower()
                if not nombre:
                    print("❌ El nombre no debe estar vacío.")
                    continue
                nombres.append(nombre)
                break
            while True:
                telefono = input("Teléfono: ").strip()
                if telefono.isdigit() and len(telefono) >= 7:
                    telefonos.append(telefono)
                    break
                else:    
                    print("❌ El teléfono solo debe tener números y tener 7 o más dígitos.")
                    continue
            while True:
                email = input("email: ").strip().lower()
                if "@" in email and "." in email:
                    emails.append(email)
                    break
                else:
                    print("El email debe tener '@' y .")
                    continue
            print(f"\nContacto: {nombre} - {telefono} - {email}. Se agregó correctamente ✅.")
        # Buscar contacto
        elif opcion == 3:
            print("\n--- BUSCAR CONTACTO ---")
            buscar = input("Buscar: ").strip().lower()
            encontrados = False
            for i, nombre in enumerate(nombres):
                if buscar in nombre.lower():
                    print(f"{i+1}. {nombre} - {telefonos[i]} - {emails[i]}")
                    encontrados = True
            if not encontrados:
                print("❌ No se encontraron contactos con ese nombre.")
                continue
                
        #Eliminar contacto
        elif opcion == 4:
            print("\n--- ELIMINAR CONTACTO ---")
            for i, nombre in enumerate(nombres):
                print(f"{i+1}. {nombre} - {telefonos[i]} - {emails[i]}")
            
            try:
                indice = int(input("Número del contacto a eliminar: ")) - 1
                if indice < 0 or indice >= len(nombres):
                    print("❌ Número inválido")
                    continue
                
                eliminado_nom = nombres.pop(indice)
                eliminado_tel = telefonos.pop(indice)
                eliminado_email = emails.pop(indice)
                print(f"✅ Contacto '{eliminado_nom}' eliminado")
            except ValueError:
                print("❌ Ingrese un número válido")
        # Salir
        elif opcion == 5:
            print("Hasta luego!")
            break

    except ValueError:
        print("❌ Ingrese una opción válida.")
    