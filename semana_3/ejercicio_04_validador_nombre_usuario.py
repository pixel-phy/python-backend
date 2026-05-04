"""Validador de nombre de usuario:
Un sistema debe validar nombres de usuarios para el registro.
Reglas:
- De 5 a 15 caracteres.
- Sólo letras minúculas, números y guion bajo.
- No puede empezar con número.
- No puede tener espacios. """

print("\n=== VALIDADOR DE NOMBRES DE USUARIOS === \n")
while True:
    nombre_usuario = input("Nombre de usuario: ").strip()

    valido = False
    primera = nombre_usuario[0]

    if len(nombre_usuario) < 5:
        motivo = 'muy corto'
        valido = False
    elif len(nombre_usuario) > 15:
        motivo = 'muy largo'
        valido = False
    else:
        valido = True
        for letra in nombre_usuario:
            if letra.isupper():
                valido = False
                motivo = 'tiene mayúscula'

    if primera.isdigit():
        valido = False
        motivo = 'empieza por número'

    if " " in nombre_usuario:
        valido = False
        motivo = 'tiene espacio'
    if valido:
        print(f"✅ {nombre_usuario}")
        break
    else:
        print(f"❌ {nombre_usuario} ({motivo})\n")
        continue
        
