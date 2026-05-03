"""Validador de contraseñas fuerte:
Un sistema de registro debe validar que la contraseña del usuario sea segura.
Reglas:
- Mínimo 8 caracteres.
- Al menos una letra mayúscula.
- Al menos una letra minúscula.
- Al menos un número. 
- Al menos un carácter especial.

Escribir un programa que pida una contraseña y valide cada regla, mostrando cuáles cumple y cuáles no."""
print("\n=== VALIDADOR DE CONTRASEÑA ===\n")

while True:
    contraseña = input("Contraseña: ").strip()
    # Inicializamos variables
    min_caracteres = len(contraseña) >= 8
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False

    #Se recorre cada caracter con ciclo for para verificar
    for letra in contraseña:
        if letra.isupper():
            tiene_mayuscula = True
        elif letra.islower():
            tiene_minuscula = True
        elif letra.isdigit():
            tiene_numero = True
        elif letra in "!@#$%^&*":
            tiene_especial = True
    
    # Mostramos resultados
    print("\n--- Validaciones ---")
    if min_caracteres:
        print("✅ Mínimo 8 caracteres")
    else:
        print("❌ Mínimo 8 caracteres")
    if tiene_mayuscula:
        print("✅ Al menos una mayúcula")
    else:
        print("❌ Al menos una mayúscula")
    if tiene_minuscula:
        print("✅ Al menos una minúscula")
    else:
        print("❌ Al menos una minúscula")
    if tiene_numero:
        print("✅ Al menos un número")
    else:
        print("❌ Al menos un número")
    if tiene_especial:
        print("✅ Al menos un carácter especial")
    else:
        print("❌ Al menos un carácter especial")

    #Verificamos que cumpla todas las reglas
    if min_caracteres and tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial:
        print("\n ✅ Contraseña segura.")
        break
    else:
        print("❌ Contraseña débil.\n")
