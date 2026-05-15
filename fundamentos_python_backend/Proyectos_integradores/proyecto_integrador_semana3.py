"""Sistema de procesamiento de usuarios para una API
1. Validar nombre: solo letras y espacios, mínimo 3 caracteres.
2. Validar email: formato estándar (tiene @, tiene . después del @).
3. Validar teléfono: solo números, opcionalemente con + al inicio.
4. Generar nombre de usuario: primeras 5 letras del nombre + últimos 3 dígitos del teléfono + dominio.
5. Mostrar informe final con todos los datos procesados."""

print("\n === SISTEMA DE REGISTRO ===\n")
while True:

    while True:
        nombre = input("Nombre: ").strip()

        # Validamos que solo tenga letras y espacios
        valido = True
        for letra in nombre:
            if not (letra.isalpha() or letra == " "):
                valido = False
                break
        if not valido:
            print("El nombre solo puede contener letras y espacios.")
            continue
        break

    while True:    
        email = input("email: ").strip()
        if not "@" in email:
            print("El correo debe contener '@'.")
            continue
        posicion = email.find("@")
        if not "." in email[posicion:]:
            print("El correo debe tener (.) después del @.")
            continue
        break

    while True:
        telefono = input("Teléfono: ").strip()
        if telefono[0] == '+' or telefono[1:].isdigit():
            break
        elif telefono.isdigit():
            break
        else:
            print("El teléfono sólo puede contener número e iniciar con '+'.")
            continue
    
    letras_nombre = nombre[0:5].lower().replace(" ", "")
    numeros_tel = telefono[-3:]
    dominio = email[posicion:]
    nombre_usuario = letras_nombre + numeros_tel + dominio
    
    print("\n--- INFORME FINAL ---\n")
    print(f"Nombre completo: {nombre}")
    print(f"EMAIL: {email}")
    print(f"Teléfono: {telefono}")
    print(f"Usuario: {nombre_usuario}")
    break
