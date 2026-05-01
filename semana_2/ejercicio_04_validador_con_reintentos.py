"""Validador de usuarios con reintentos:
Un sistema de login permite 3 intentos para ingresar usuario y contraseña. 
Si falla 3 veces, bloquea el acceso. 

Requisitos:
1. Credenciales correctas preferidas:
- Usuario: "admin"
- Contraseña: "1234" 
2. Validaciones:
- Usuario y contraseña no pueden estar vacíos
- Usuario y contraseña no pueden tener espacios al inicio o final.
3. Comportamientos:
- Máximo tres intentos.
- Por cada intento fallido, mostrar intentos restantes. 
- Si se agotan los intentos -> "❌ Cuenta bloqueda"
4. Además:
- Usar for con range() para controlar intentos. 
- Usar break si el acceso es exitoso.
- Usar continue si algún campo está vacío (sin contar como intento)"""

print("\n--- Validador de intentos usuario ---\n")
#Entradas
for intento in range(1, 4):
    print(f"Intento {intento} de 3\n")
    entrada_usuario = input("Usuario: ").strip().lower()
    while entrada_usuario == "":
        print("Usuario vacío. Intente de nuevo.\n")
        entrada_usuario = input("Usuario: ").strip().lower()
        continue
    entrada_contraseña = input("Contraseña: ").strip()
    while entrada_contraseña == "":
        print("Contraseña vacía. Intente nuevamente.\n")
        break
    if entrada_usuario == "admin" and entrada_contraseña == "1234":
        print("✅ Acceso concedido.")
        break
    elif entrada_usuario != "admin" and entrada_contraseña == "1234":
        print(f"Usuario incorrecto! Te quedan {3 - intento} intentos.\n")
        continue
    elif entrada_usuario == "admin" and entrada_contraseña != "1234":
        print(f"Contraseña incorrecta! Te quedan {3 - intento} intentos.\n")
        continue
    elif intento == 3:
        print(f"\nTe quedan {3 - intento} intentos.")
        print("\n❌ Cuenta bloqueada.\n")
    else:
        print(f"Contraseña y usuarios incorrectos! Te quedan {3 - intento} intentos.\n")
        continue
