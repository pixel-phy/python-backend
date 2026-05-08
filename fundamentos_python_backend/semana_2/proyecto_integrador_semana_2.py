"""Sistema bancario simulado:
Un cajero automático necesita un sistema que valide al usuario y permita operaciones bancarias básicas.
Requisitos:
Fase 1: Validación de tarjeta (fuera del bucle principal).
1. Pedir número de la tarjeta (16 dígitos, puede tener espacios)
2. Validar:
- Que tenga exactamente 16 dígitos después de eliminar espacios.
- Que solo contenga números.
- Identificar el tipo (Visa, MasterCard, American Express, Deconocido) usando los primeros códigos:
 4 para Visa, 51, 52, 53, 54 y 55 para MasterCard, 34 o 37 American Express.
 3. Si la tarjeta no es válida, el programa termina. Si es válida, mostrar el tipo y continuar.
 
 Fase 2: Validación de PIN (3 Intentos).
 1. Pin correcto: "1234".
 2. Dar 3 intentos para ingresar el PIN.
 3. Si acierta: Acceso concedido y continuar.
 4. Si falla los 3 intentos: Cuenta bloqueada y el programa termina.
 
 Fase 3: Menú Principal (Se repite hasta salir).
 El usuario tiene un saldo inicial de $5000:
 Opciones del Menú:
 1. Consultar saldo.
 2. Depositar dinero.
 3. Retirar dinero.
 4. Ver últimos movimientos (Últimas 5 operaciones).
 5. Salir.
 
 Reglas de cada opción:
 Opción 1 - Consultar saldo
 Mostrar saldo actual.
 
 Opción 2 - Depositar
 - Pedir monto a depositar (debe ser positivo).
 - Sumar al saldo.
 - Registrar movimiento: "Depósitos: +$XXX" 
 
 Opción 3 - Retirar
 - Pedir monto a retirar (debe ser positivo).
 - Validar que no se supere el saldo disponible.
 - Restar del saldo.
 - Registrar movimiento: "Retiro: -$XXX".
 
 Opción 4 - Ver últimos movimientos
 - Mostrar las últimas 5 operaciones realizadas (máximo 5).
 - Si no hay movimientos, mostrar "No hay movimientos registrados".
 
 Opción 5 - Salir
 - Mostrar mensaje de despedida y terminar el programa."""

print("\n=== CAJERO AUTOMÁTICO ===\n")
# Fase 1:
entrada_numero_tarjeta = input("Número de la tarjeta (XXXX XXXX XXXX XXXX): ").strip()
numero_tarjeta = entrada_numero_tarjeta.replace (" ", "") # Eliminamos los espacios.
if len(numero_tarjeta) != 16:
    print("El número de la tarjeta debe tener 16 dígitos.")
    exit()
if not numero_tarjeta.isdigit():
    print("Los dígitos sólo pueden ser números.")
    exit()

# Tipo de tarjeta
primer_digito = numero_tarjeta[0]
primeros_dos = numero_tarjeta[0:2]

if primer_digito == '4':
    tipo_tarjeta = "Visa"
    print(f"✅ Tarjeta válida. Tipo: {tipo_tarjeta}")
elif primeros_dos >= '51' and primeros_dos <= '55':
    tipo_tarjeta = "MasterCard"
    print(f"✅ Tarjeta válida. Tipo: {tipo_tarjeta}")
elif primeros_dos == '34' or primeros_dos == '37':
    tipo_tarjeta = "American Express"
    print(f"✅ Tarjeta válida. Tipo: {tipo_tarjeta}")
else:
    tipo_tarjeta = "Desconocido"
    print(f"✅ Tarjeta válida, pero de tipo {tipo_tarjeta}")

# Fase 2: Validación de Pin
print("\n=== Validación de PIN ===\n")
pin_correcto = "1234"

for intento in range(1, 4):
    print(f"Intento {intento} de 3\n")
    entrada_pin = input("PIN: ").strip()
    if entrada_pin != pin_correcto:
        intentos_restantes = 3 - intento
        if intentos_restantes > 0:
            print(f"❌ PIN incorrecto. Tiene {intentos_restantes} intentos disponibles.\n")
        else:
            print("\n❌ Cuenta bloqueada.\n")
            exit()
    else:
        print("\n✅ Acceso concedido\n")
        break

#Inicialización de variables
saldo = 5000.0
movimientos = ""

#Fase 3: Menú principal
while True:
    print("\n=== MENÚ PRINCIPAL ===\n")
    print("1. Consultar saldo.")
    print("2. Depositar dinero.")
    print("3. Retirar dinero.")
    print("4. Ver últimos movimientos.")
    print("5. Salir.\n")

    opcion = input("Opción: ").strip()

    if opcion == '1':
        print(f"\nSaldo actual: ${saldo:.2f}")
        movimientos += f"| Saldo: {saldo:.2f}"
    elif opcion == '2':
        try: 
            deposito = float(input("\nCantidad a depositar: "))
            if deposito < 0:
                print("El depósito debe ser mayor que 0.")
                continue
            saldo += deposito
            movimientos += f"| Depósito +${deposito:.2f}"
            print(f"\nDepositaste: ${deposito:.2f}")
        except ValueError:
            print("\nIngrese un número válido.")
    elif opcion == '3':
        try:
            retiro = float(input("\nCantidad a retirar: "))
            if retiro <= 0:
                print("El monto debe ser mayor a 0\n")
                continue
            if retiro > saldo:
                print("Saldo insuficiente\n")
                continue
            saldo -= retiro
            movimientos += f'| Retiro: -${retiro:.2f}'
            print(f"\nRetiraste: {retiro:.2f}")
        except ValueError:
            print("Ingrese un número válido.\n")
    elif opcion == '4':
        if movimientos == "":
            print("\nNo hay movimientos registrados")
        else:
            print(f"Últimos movimientos: {movimientos}")
    elif opcion == '5':
        print ("\nGracias por utilizar nuestros cajeros.")
        break
    else:
        print("\nOpción no disponible.")