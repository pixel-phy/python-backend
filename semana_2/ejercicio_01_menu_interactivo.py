"""Menú interactivo:
Un cajero automático necesita un menú que se repita hasta que el usuario elija salir:
# Mostrar este menú:
=== CAJERO AUTOMÁTICO ===
1. Ver saldo
2. Depositar dinero
3. Retirar dinero
4. Salir

# Reglas:
- Saldo inicial: $1000
- Al depositar: sumar al saldo
- Al retirar: restar del saldo (no puede quedar negativo)
- Si elige opción inválida: mostrar "Opción no válida"
- El menú se repite hasta que elige 4 (Salir)
- Al salir: mostrar "Gracias por usar el cajero"

# Validaciones:
- La opción debe ser 1, 2, 3 o 4
- El monto a retirar no puede ser mayor al saldo
- El monto a depositar debe ser > 0"""

print("\n=== CAJERO AUTOMÁTICO ===\n")
saldo = 1000.0

while True:
    print("\n--- Menú Principal ---")
    print("1. Ver saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Ingrese una opción (1-4): ").strip()

    if opcion == "1":
        print(f"Saldo actual: ${saldo:.2f}")

    elif opcion == "2":
        try:
            deposito = float(input("Cantidad a depositar: "))
            if deposito <= 0:
                print("El monto debe ser mayor a 0")
                continue
            saldo += deposito
            print(f"Depositaste ${deposito:.2f}")
        except ValueError:
            print("Ingrese un número válido")

    elif opcion == "3":
        try:
            retiro = float(input("Cantidad a retirar: "))
            if retiro <= 0:
                print("El monto debe ser mayor a 0")
                continue
            if retiro > saldo:
                print("Saldo insuficiente")
                continue
            saldo -= retiro
            print(f"Retiraste ${retiro:.2f}")
        except ValueError:
            print("Ingrese un número válido")

    elif opcion == "4":
        print("Gracias por usar el cajero")
        break

    else:
        print("Opción no válida")