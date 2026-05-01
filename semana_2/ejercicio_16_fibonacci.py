"""Fibonacci:
Generar secuencias (números de identificación, tokens, etc) y manejar algoritmos básicos.
1. Solicitar un número N (entero positivo).
2. Mostrar los primeros N números de la serie Fibonacci."""

print("\n === FIBONACCI ===\n")
# Bucle principal
while True:
    entrada = input("N: ")
    try:
        numero = int(entrada)
        if numero < 0:
            print("El número debe ser un entero positivo.")
            continue

        a, b = 0, 1
        resultado = ""

        for i in range(numero):
            if i == numero - 1:
                resultado += str(a) # Último valor sin coma
            else:
                resultado += str(a) + ", "
            a , b = b, a + b
        print("\n--- RESULTADO ---\n")
        print(f"Los primeros {numero} números de Fibonacci son: ")    
        print(resultado)
        break
    except ValueError:
        print("Ingrese un número válido.\n")
