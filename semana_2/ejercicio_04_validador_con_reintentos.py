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

print("\n=== VALIDADOR DE LOGIN ===\n")

usuario_correcto = "admin"
contrasena_correcta = "1234"

for intento in range(1, 4):
    print(f"Intento {intento} de 3\n")
    
    # Validar usuario (no vacío)
    entrada_usuario = input("Usuario: ").strip().lower()
    while entrada_usuario == "":
        print("❌ Usuario vacío. Intente de nuevo.\n")
        entrada_usuario = input("Usuario: ").strip().lower()
    
    # Validar contraseña (no vacía)
    entrada_contrasena = input("Contraseña: ").strip()
    while entrada_contrasena == "":
        print("❌ Contraseña vacía. Intente de nuevo.\n")
        entrada_contrasena = input("Contraseña: ").strip()
    
    # Verificar credenciales
    if entrada_usuario == usuario_correcto and entrada_contrasena == contrasena_correcta:
        print("✅ Acceso concedido")
        break
    else:
        intentos_restantes = 3 - intento
        if intentos_restantes > 0:
            print(f"❌ Credenciales incorrectas. Te quedan {intentos_restantes} intento(s)\n")
        else:
            print("❌ Cuenta bloqueada")