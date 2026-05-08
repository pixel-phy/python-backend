"""Menú con constraseña:
Un programa que no permite el acceso hasta que el usuario ingrese la contraseña correcta. 
Una vez dentro, muestra un menú y se ejecuta hasta que elija salir.

Requisitos:
1. Primera fase: validar contraseña.
- Contraseña correcta: "python123"
- Usar while para repetir hasta que sea correcta
- Si es correcta, mostrar "✅ Acceso concedido" y continuar

Segunda fase: menú principal
- Opciones:
1. Ver mensaje correcto.
2. Cambiar contraseña.
3. Salir.
- El menú se repite hasta que escriba salir.
- Usar while o for para mantener menú activo.

Reglas adicionales:
- Si elige opción 1: mostrar "🔐 El mensaje secreto es: Python es genial"
- Si elige opción 2: pedir nueva contraseña (mínimo 6 catacteres) y actualizar
- Si elige opción 3: mostrar "👋 Hasta luego" y terminar. """

print("\n=== MENÚ CON CONTRASEÑA ===\n")
contraseña_correcta = "python123"

# Validar contraseña
while True:
    contraseña = input("Contraseña: ").strip().lower()
    if contraseña == contraseña_correcta:
        print("✅ Acceso concedido")
        break
    else:
            print("¡Contraseña incorrecta!")
# Menú principal
while True:        
    print("\n--- Menú principal ---\n")
    print("1. Ver mensaje secreto.")
    print("2. Cambiar contraseña.")
    print("3. Salir.")
    
    opcion = input("\n Opción: ").strip()

    if opcion == '1':
         print("🔐 El mensaje secreto es: Python es genial")
    elif opcion == '2':
         while True:
              nueva = input("Nueva contraseña (mínimo 6 caracteres): ").strip()
              if len(nueva) < 6:
                   print("La contraseña debe tener mínimo 6 caracteres.")
              else:
                   contraseña_correcta = nueva
                   print("✅ Contraseña actualizada")
                   break
    elif opcion == '3':
         print("👋 Hasta luego")
         break
    
    else:
         print("Opción no válida.")
         


