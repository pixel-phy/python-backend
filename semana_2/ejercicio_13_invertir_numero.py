"""Invertir un número:
Un programa que toma un número entero y muestra su versión invertida.
Requisitos:
- Pedir un número entero positivo.
- Usar el bucle while para invertir el número (sin convertirlo a string)
- Mostrar el resultado. """
print("\n=== INVERTIR UN NÚMERO ===\n")
invertido = 0
while True:
    entrada = input("Número entero positivo: ").strip()
    try:
        numero = int(entrada)
        if numero < 0:
            print("El número debe ser positivo.")
        else:
            while numero > 0:
                digito = numero % 10 # Último digito
                invertido = invertido * 10 + digito
                numero = numero // 10 # Eliminamos último digito
            
            print(f"Invertido: {invertido}")
            break
    except ValueError:
        print("Ingrese un número entero válido.")

