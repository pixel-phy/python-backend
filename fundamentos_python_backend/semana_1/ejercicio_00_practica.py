"""Escribe un programa que:

1. Pregunte al usuario su nombre, edad y altura en metros.

2. Use f-strings para mostrar:

"Hola [nombre], tienes [edad] años"

"Tu altura es [altura]m"

"En 5 años tendrás [edad+5] años"

Al mostrar la altura, redondea a 2 decimales

Si el usuario no escribe nada (entrada vacía), muestra "Dato inválido" y termina."""

print("\n=== Primera práctica Backend ===\n")
# Usuario ingresa nombre
entrada1 = input("Ingresa tu nombre: ").strip()
if entrada1 == "":
    print("Dato inválido.")
    exit()
else:
    nombre = str(entrada1)

# Usuario ingresa edad
entrada2 = input("Ingresa tu edad: ").strip()
if entrada2 == "":
    print("Dato inválido.")
    exit()
else:
    try: 
        edad = int(entrada2)
    except ValueError:
        print("Debes ingresar un número entero.")
        exit()

# Usuario ingresa altura en m
entrada3 = input("Ingresa tu altura en metros: ").strip()
if entrada3 == '':
    print("Dato inválido.")
    exit()
else:
    try:
        altura = float(entrada3)
    except ValueError:
        print("Debes ingresar un número float.")
        exit()

# Mostramos resultados en pantalla
print(f"Hola {nombre}, tienes {edad} años.")
print(f"Tu altura es {altura:.2f} m.")
print(f"En 5 años tendrás {edad+5} años.")