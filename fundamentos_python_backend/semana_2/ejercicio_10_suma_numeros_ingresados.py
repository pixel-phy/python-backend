"""Escribe un programa que pida números hasta que el usuario ingrese 0, y luego muestre la suma."""
# Inicializamos variables
suma = 0
contador = 1
cantidad = 0

#Bucle principal
while True:
    entrada = input(f"Número {contador} (0 para salir): ").strip()
    try:
        numero = int(entrada)
        if numero == 0:
            break
        else:
            suma += numero
            contador += 1
            cantidad += 1
    except ValueError:
        print("Debes ingresar un número.")

print("\n---RESULTADOS---\n")
print(f"Ingresaste: {cantidad} números.")
print(f"La suma es: {suma}")