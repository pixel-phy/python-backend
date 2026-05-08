"""Analizador de números:
Un programa que pide números hasta que el usuario decide terminar, y luego muestra análisis completo.
Requisitos:
1. Pedir números.
2. Validar que sea un número válido.
3. Preguntar después de cada número: ¿Otro número? (s/n).
4. Acumular/Calcular:
- Cantidad de número ingresados.
- Suma total.
- Promedio.
- Número más alto.
- Número más bajo.
- Cantidad de número pares.
- Cantidad de números mayores al promedio."""

print("\n === ANALIZADOR DE NÚMEROS ===\n")
# Inicializamos variables
total = 0
cantidad_total = 0
cantidad_pares = 0
mas_alto = float("-inf")
mas_bajo = float("inf")
contador = 1
# Bucle principal
while True:
    entrada = input(f"Número ({contador}): ")
    try:
        numero = float(entrada)
        print(f"\nEl {numero} es un número válido\n")
        total += numero
        cantidad_total += 1
        contador += 1
        if numero > mas_alto:
            mas_alto = numero
        if numero < mas_bajo:
            mas_bajo = numero
        if numero % 2 == 0:
            cantidad_pares += 1
        
        # Otro número
        repetir = input("\n¿Otro número? (s/n): ").strip().lower()
        if repetir != 's':
            break

    except ValueError:
        print("Debes ingresar un número válido.")

print("\n--- RESULTADOS ---\n")
print(f"Números ingresados: {cantidad_total}")
print(f"Suma total: {total}")
print(f"Promedio: {total / cantidad_total:.2f}")
print(f"Número más alto: {mas_alto}")
print(f"Número más bajo: {mas_bajo}")
print(f"Cantidad de números pares: {cantidad_pares}")
print(f"Cantidad de números impares: {cantidad_total - cantidad_pares}")
