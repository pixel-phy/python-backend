"""Escribe un programa que:
1. Pida dos números enteros (con validación)
2. Muestre: suma, resta, multiplicación, división exacta, división entera, resto y potencia.
3. Si el segundo número es 0, evita la división y muestra "No se puede dividir por 0 """

print("\n=== Práctica 2: Operadores ===\n")
# Primer número
entrada1 = input("Ingresa el primer número: ").strip()
try: 
    numero1 = float(entrada1)
except ValueError:
    print("Por favor ingresa un número válido.")
    exit()

# Segundo número
entrada2 = input("Ingresa el segundo número: ").strip()
try:
    numero2 = float(entrada2)
    if numero2 == 0:
        print("No se puede devidir por 0.")
        exit()
except ValueError:
    print("Por favor ingresa un número válido.")
    exit()

# Hacemos operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
division_entera = numero1 // numero2
modulo = numero1 % numero2
potencia = numero1 ** numero2

# Mostramos resultados

print("--- Resultados ---")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"División entera: {division_entera}")
print(f"Módulo: {modulo}")
print(f"Potencia: {potencia}")
