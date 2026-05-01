""" Adivina el número con límite de intentos:
Escribe un código completo usando for, break, else en for y validaciones."""
import random

secreto = random.randint(1, 20)
print("\n === ADIVINA EL NÚMERO ===\n")
print("Tienes 5 intentos para adivinar el número entre 1 y 20.")

for intento in range(1, 6):
    print(f"Intento {intento} de 5")

    entrada = input("Número: ").strip()

    try:
        numero = int(entrada)
        if numero < 1 or numero > 20:
            print("El número debe estar entre 1 y 20.")
            continue
    except ValueError:
        print("Debe ingresar un número entero.")
        continue

    if numero == secreto:
        print(f"Correcto! El número era {secreto}")
        break
    else:
        print(f"Incorrecto. Te quedan {5 - intento} intentos.")
else:
    # Si el for termina sin break
    print(f"\n Perdiste! El número era {secreto}")