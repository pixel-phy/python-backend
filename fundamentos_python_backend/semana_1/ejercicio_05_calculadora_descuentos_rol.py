"""Estás desarrollando el sistema de descuentos para una tienda online. 
Los clientes tienen diferentes roles y reciben descuentos según su rol y el monto de su compra.

Reglas de descuento
Rol	        Condición	        Descuento
admin	    Cualquier monto	    30%
premium	    Compra ≥ $100	    20%
premium	    Compra < $100	    10%
regular	    Compra ≥ $200	    5%
regular	    Compra < $200	    0%
invitado	Cualquier monto	    0% 

Si después de aplicar el descuento el total final supera los $1000, se aplica un 5% extra de descuento.

Requisitos del programa
Solicitar al usuario:
1. Rol (admin, premium, regular, invitado)
2. Monto de la compra (número positivo)

Validar:
1. Que el rol sea uno de los permitidos.
2. Que el monto sea un número mayor a 0

Calcular y mostrar:
1. Monto original.
2. Porcentaje de descuento aplicado.
3. Monto del descuento (en valor numérico).
4. Monto final después del descuento.

Si aplicó el descuento extra del 5%, indicarlo"""

print("\n=== Calculadora de descuentos por rol ===\n")
print("Escribe 'salir' para finalizar el programa.\n")

while True:
    # 1. Solicitar rol
    rol_usuario = input("Ingresa tu rol (admin/premium/regular/invitado): ").strip().lower()
    
    if rol_usuario == 'salir':
        print("Saliste del programa.")
        break
    
    # Validar rol
    if rol_usuario not in ['admin', 'premium', 'regular', 'invitado']:
        print("Rol no válido. Los roles permitidos son: admin, premium, regular, invitado\n")
        continue
    
    # 2. Solicitar monto
    entrada_monto = input("Monto de la compra: ").strip()
    
    try:
        monto_original = float(entrada_monto)
        if monto_original <= 0:
            print("El monto debe ser mayor a 0.\n")
            continue
    except ValueError:
        print("❌ Debes ingresar un número válido.\n")
        continue
    
    # 3. Calcular descuento según rol
    if rol_usuario == 'admin':
        porcentaje_rol = 30
    elif rol_usuario == 'premium':
        if monto_original >= 100:
            porcentaje_rol = 20
        else:
            porcentaje_rol = 10
    elif rol_usuario == 'regular':
        if monto_original >= 200:
            porcentaje_rol = 5
        else:
            porcentaje_rol = 0
    else:  # invitado
        porcentaje_rol = 0
    
    # 4. Calcular descuento por rol
    descuento_rol = monto_original * porcentaje_rol / 100
    monto_despues_rol = monto_original - descuento_rol
    
    # 5. Verificar si aplica descuento extra (5% si el monto DESPUÉS del rol supera $1000)
    if monto_despues_rol > 1000:
        porcentaje_extra = 5
        descuento_extra = monto_despues_rol * porcentaje_extra / 100
        monto_final = monto_despues_rol - descuento_extra
        aplica_extra = "Sí aplica"
    else:
        porcentaje_extra = 0
        descuento_extra = 0
        monto_final = monto_despues_rol
        aplica_extra = "No aplica"
    
    # 6. Mostrar resultados
    print("\n--- Resultados ---")
    print(f"Monto original: ${monto_original:.2f}")
    print(f"Descuento por rol ({porcentaje_rol}%): ${descuento_rol:.2f}")
    
    if aplica_extra == "Sí aplica":
        print(f"Descuento extra ({porcentaje_extra}% por superar ${monto_despues_rol:.2f}): ${descuento_extra:.2f}")
    else:
        print(f"Descuento extra: No aplicó")
    
    print(f"Monto final: ${monto_final:.2f}")
    
    # 7. Preguntar si continuar
    print()
    repetir = input("¿Hacer otro cálculo? (s/n): ").strip().lower()
    if repetir != 's':
        print("\nGracias por utilizar nuestra calculadora.")
        break
    
    print()  # Línea en blanco antes de siguiente iteración