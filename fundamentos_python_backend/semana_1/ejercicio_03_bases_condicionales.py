""" Escribe un programa que simule un sistema de validación de acceso a contenido:
Enunciado:
1. Preguntar edad del usuario (entero)
2. Preguntar si tiene membresía activa (escribe "si" o "no")
3. Preguntar si el contenido es para adultos (escribe "si" o "no")

Reglas de acceso:
1. Si el contenido NO es para adultos → acceso PERMITIDO (sin importar edad)
2. Si el contenido ES para adultos:
3. Edad mayor o igual a 18 Y tiene membresía → acceso PERMITIDO
4. Edad mayor o igual a 18 pero NO tiene membresía → "Necesitas membresía"
5. Edad menor a 18 → "Acceso denegado: contenido solo para mayores de 18"

Requisitos técnicos:
1. Usar if/elif/else
2. Usar operadores lógicos (and, or, not)
3. Validar que la edad sea un número positivo
4. Validar que la respuesta de membresía/contenido sea "si" o "no"

Mostrar mensajes claros"""
print("\n=== Ejercicio 03. Condicionales ===\n")

# preguntamos edad
try:
    edad = int(input("Ingresa tu edad: ").strip())
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
except ValueError:
    print("Valor inválida.")
    exit()

# preguntamos membresía
membresia = input("¿Tiene membresía activa? (si/no): ").strip().lower()
if membresia not in ('si', 'no'):
    print("Opción inválida")
    exit()
membresia = membresia == 'si'  # Se convierte a booleano

# preguntamos si el contenido es para adultos
contenido_adultos = input("El contenido es para adultos (si/no): ").strip().lower()
if contenido_adultos not in ('si', 'no'):
    print("Opción inválida")
    exit()
contenido_adultos = contenido_adultos == 'si'

# Lógica
if not contenido_adultos or (edad >= 18 and membresia):
    print("Acceso permitido!")
elif edad >= 18:
    print("Necesitas membresía.")
else:
    print("Acceso denegado: contenido solo para mayores de 18 años.")