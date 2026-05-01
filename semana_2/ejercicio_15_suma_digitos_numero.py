"""Suma de dígitos de un número:
Calcular el checksum (dígito verificador) o sumar valores numéricos extraídos de un identificador.
Escribe un programa que:
1. Solicite un número entero positivo al usuario.
2. Calcule la suma de sus dígitos utilizando un bucle (No se vale convertir a string y sumar con for)
3. Muestre el resultado."""

print("\n=== SUMA DE DÍGITOS ===\n")
#Bucle principal
while True:
    entrada = input("Número positivo: ")
    try:
        numero = int(entrada)
        if numero < 0:
            print("El número debe ser positivo.")
            continue
        
        # Inicializamos variables
        numero_original = numero
        suma = 0
        while numero > 0:
            digito = numero % 10 # Toma el último digito
            suma += digito # Lo acumulamos
            numero //= 10 # Elimina el último digito hasta que no quede ninguno
        break
    except ValueError:
        print("Ingrese un número válido.")

print("\n--- RESULTADOS ---\n")
print(f"Número: {numero_original}")
print(f"Sus dígitos suman: {suma}")