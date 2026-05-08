"""Número primo:
Un programa que determina si un número es primo o no.
Requisitos:
- Pedir un número entero positivo.
- Validar que sea mayor que 1.
- Usar for y range() para verificar si tiene divisores
- Mostrar "✅ Es primo" o "❌ No es primo".
"""
print("\n === VERIFICADOR DE NÚMEROS PRIMOS ===\n")
while True:
    entrada = input("Número entero positivo: ").strip()
    try:
        numero = int(entrada)
        if numero <= 1:
            print("El número debe ser mayor que 1.")
            continue

        # Verificamos si es primo
        es_primo = True
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            print(f"El número {numero} es primo.")
        else:
            print(f"El número {numero} no es primo.")

        break
       
    except ValueError:
        print("Ingrese un número válido.")