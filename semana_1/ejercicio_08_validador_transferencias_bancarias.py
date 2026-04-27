"""  Contexto: Un banco valida transferencias entre cuentas.
Reglas:
1. Si el monto es mayor a $10,000 → requiere autorización especial
2. Si la cuenta de destino es la misma que la de origen → error: "No puedes transferirte a ti mismo"
3. Si el monto es negativo o cero → error
4. Si el saldo es insuficiente → error
5. Mostrar mensaje de éxito si pasa todas las validaciones

Datos de entrada:
1. Saldo disponible
2. Cuenta origen
3. Cuenta destino
4. Monto a transferir."""

print("\n=== VALIDADOR TRANSFERENCIAS BANCARIAS ===\n")

# Saldo disponible
entrada_saldo = input("Saldo disponible: ").strip()
try:
    saldo_disponible = float(entrada_saldo)
    if saldo_disponible <= 0:
        raise ValueError("El saldo disponible debe ser mayor que 0.")
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Cuenta origen y destino
cuenta_origen = input("Cuenta origen: ").strip()
cuenta_destino = input("Cuenta destino: ").strip()

if cuenta_origen == cuenta_destino:
    print("Error: No puedes transferirte a ti mismo.")
    exit()

# Monto a transferir
entrada_monto = input("Monto a transferir: ").strip()
try:
    monto_transferir = float(entrada_monto)
    if monto_transferir <= 0:
        raise ValueError("El monto a transferir debe ser mayor que 0.")
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Validaciones en orden lógico
if saldo_disponible < monto_transferir:
    print("Error: Saldo insuficiente")
elif monto_transferir >= 10000:
    print("Requiere autorización especial")
else:
    print("¡Transferencia exitosa!")