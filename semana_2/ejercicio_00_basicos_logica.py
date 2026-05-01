""" Ejercicios cortos para coger el ritmo de cómo empezar."""
# Mostrar números pares del 2 al 20
print("Números pares del 2 al 20.")
for num in range(2, 21, 2):
    print(num)

# Sumar los números del 1 al 100
print("\nSuma números del 1 al 100.\n")
total = 0
for sum in range(1, 101):
    total += sum
print(total)

# Pedir un número hasta que sea positivo
while True:
    numero = int(input("Número positivo: "))
    if numero > 0:
        break
    print("Error, intente nuevamente.")

# mostrar hola 5 veces
for i in range(5):
    print("Hola")

# Mostrar cuántos números ingresan
contador = 0
while True:
    n = int(input("Número (0 para terminar): "))
    if n == 0:
        break
    contador += 1

print(f"Ingresaste {contador} números.")

