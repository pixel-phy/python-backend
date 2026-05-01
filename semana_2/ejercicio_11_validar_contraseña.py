"""Validar contraseña con reintentos:
Un programa que:
- Pide contraseña (la contraseña correcta es: "secreto123")
- De 3 intentos máximos
- Si acierta:"✅ Acceso concedido"
- Si falla los 3: "❌ Demasiados intentos. Cuenta bloqueada". """

print("\n=== VALIDADOR DE CONTRASEÑA ===\n")
#Inicializamos variables
contraseña_correcta = "secreto123"
max_intentos = 3

for intento in range(1, max_intentos + 1):
    print(f"\nIntento {intento} de {max_intentos}")
    contraseña = input("Contraseña: ").strip()

    if contraseña == contraseña_correcta:
        print("✅ Acceso concedido")
        break
    else:
        print("❌ Contraseña incorrecta!")
else:
    print("❌ Demasiados intentos. Cuenta bloqueada")
