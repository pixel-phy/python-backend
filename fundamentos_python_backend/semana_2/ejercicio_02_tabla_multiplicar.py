"""Tabla de multiplicar:
Un programa que muestra la tabla de multiplicar de un número ingresado por el usuario.
Requisitos:
1. Solicitar el número al usuario.
2. Validar que sea un número entero positivo (1 en adelante).
3. Mostrar la tabla del 1 al 10 usando for con range().
4. Preguntar si quiere ver otra tabla (s/n).
5. Si responde "s", tepetir todo el proceso.
6. Si responde "n", mostrar el mensaje de despedida y terminar."""

#Entrada y validación
print("\n--- TABLA DE MULTIPLICAR ---\n")
while True:

    try:
        numero = int(input("\nNúmero: "))
        if numero <= 1:
            raise ValueError ("El número debe ser mayor que 1.")
    except ValueError as e:
        print(f"Error: {e}")
        continue
    # Tabla de multiplicar
    for num in range(1, 11):
        multiplicacion = num * numero
        print(f"{numero} * {num} = {multiplicacion}")
    repetir = input("¿Quiere ver otra tabla? (s/n): ").strip().lower()
    if repetir != 's':
        print("Gracias por utilizar la tabla. Hasta la próxima!")
        break