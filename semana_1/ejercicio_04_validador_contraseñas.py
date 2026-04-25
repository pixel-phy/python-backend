"""Contexto: Un sistema debe rechazar contraseñas débiles. Estás desarrollando el sistema de registro de usuarios para una plataforma de streaming. 
El equipo de seguridad exige que las contraseñas cumplan ciertos requisitos mínimos para evitar cuentas vulnerables.

Requisitos de la contraseña
Debe cumplir TODAS las siguientes reglas para ser aceptada:
1. Longitud mínima: Al menos 8 caracteres
2. Al menos un número: Debe contener algún dígito (0-9)
3. Al menos una mayúscula: Debe contener alguna letra en mayúscula (A-Z)
4. Palabras prohibidas: No puede ser exactamente "password" ni "12345678" (sin importar mayúsculas/minúsculas)
Comportamiento esperado
El programa solo pide la contraseña una vez

Si la contraseña cumple todo → muestra "✅ Contraseña segura" y termina

Si la contraseña NO cumple → muestra todos los requisitos que faltan"""

print("\n=== Validador de contraseñas ===\n")
# Ingresa la contraseña
contraseña = input("Ingresa la contraseña: ").strip()

# Longitud
longitud_ok = len(contraseña) >= 8

# Tiene al menos un número
tiene_numero = ('0' in contraseña or '1' in contraseña or '2' in contraseña or '3' in contraseña or
                '4' in contraseña or '5' in contraseña or '6' in contraseña or '7' in contraseña or
                '8' in contraseña or '9' in contraseña)

# Tiene mayúsculas
tiene_mayusculas = ('A' in contraseña or 'B' in contraseña or 
                    'C' in contraseña or 'D' in contraseña or
                    'E' in contraseña or 'F' in contraseña or 
                    'G' in contraseña or 'H' in contraseña or
                    'I' in contraseña or 'J' in contraseña or
                    'K' in contraseña or 'L' in contraseña or
                    'M' in contraseña or 'N' in contraseña or
                    'Ñ' in contraseña or 'O' in contraseña or 
                    'P' in contraseña or 'Q' in contraseña or 
                    'R' in contraseña or 'S' in contraseña or
                    'T' in contraseña or 'U' in contraseña or
                    'V' in contraseña or 'X' in contraseña or 
                    'Y' in contraseña or 'Z' in contraseña)

#Palabras prohibidas
tiene_prohibidas = (contraseña.lower() == 'password' or
                    contraseña.lower() == '12345678')

# Hacemos validaciones
if longitud_ok and tiene_numero and tiene_mayusculas and not tiene_prohibidas:
    print("Contraseña segura!")
else:
    print("La contraseña no cumple. Requisitos que faltan:")
    if not longitud_ok:
        print("Debe contener mínimo 8 caracteres.")
    if not tiene_numero:
        print("Debe contener un número.")
    if not tiene_mayusculas:
        print("Debe contener alguna letra mayúscula.")
    if tiene_prohibidas:
        print("No debe ser 'password' o '12345678'.")