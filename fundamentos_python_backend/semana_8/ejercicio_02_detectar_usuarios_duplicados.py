"""Detectar usuarios duplicados
Un sistema recibe una lista de usuarios con posibles duplicados y necesita:
- Eliminar duplicados
- Verificar rápidamente si un usuario ya existe"""

registros = ["ana@mail.com", "luis@mail.com", "ana@mail.com", "carlos@mail.com", "luis@mail.com"]

# Eliminamos los duplicados utilizando sets
sin_duplicados = set(registros)
print(f"Correos únicos: {sin_duplicados}")

# Verificamos si un correo ya está registrado
nuevo = "ana@mail.com"
if nuevo in sin_duplicados:
    print(f"❌ El correo {nuevo} ya está registrado")
else:
    print(f"✅ El correo {nuevo} está disponible")

nuevo2 = "sofia@mail.com"
if nuevo2 in sin_duplicados:
    print(f"❌ El correo {nuevo2} ya está registrado")
else:
    print(f"✅ El correo {nuevo2} está disponible")

# Pida al usuario un correo nuevo:
while True:
    nuevo3 = input("\nCorreo nuevo: ")
    if nuevo3 in sin_duplicados:
        print(f"El correo ya está registrado. Ingrese uno diferente")
        continue
    sin_duplicados.add(nuevo3)
    print("✅ El correo se registró existosamente")
    break

print(f"Correos registrados: {sin_duplicados}")