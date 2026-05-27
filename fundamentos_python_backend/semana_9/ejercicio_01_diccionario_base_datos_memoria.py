"""Diccionario como base de datos en memoria
Simular una base de datos de usuarios usando un diccionario. """

# Base de datos de usuarios (diccionario anidado)
usuarios = {
        "ana123": {"nombre": "Ana", "edad": 25, "email": "ana@mail.com"},
        "luis456": {"nombre": "Luis", "edad": 30, "email": "luis@mail.com"},
        "carlos789": {"nombre": "Carlos", "edad": 28, "email": "carlos@mail.com"},
        }

# 1. Mostrar todos los usuarios
print("=== USUARIOS REGISTRADOS ===")
for username, datos in usuarios.items():
    print(f"@{username}: {datos['nombre']} ({datos['edad']} años) - {datos['email']}")

# 2. Buscar usuario por username
buscar = input("\nIngrese username: ")
if buscar in usuarios:
    print(f"Usuario encontrado: {usuarios[buscar]}")
else:
    print(f"Usuario '{buscar}' no encontrado")

# 3. Agregar nuevo usuario
print("\n=== REGISTRO DE NUEVO USUARIO ===")
nuevo_user = input("Username: ")
if nuevo_user in usuarios:
    print(f"El username '{nuevo_user}' ya existe")
else:
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    email = input("Email: ")
    usuarios[nuevo_user] = {"nombre": nombre, "edad": edad, "email": email}
    print(f"Usuario '{nuevo_user}' registrado exitosamente")

# 4. Mostrar usuarios actualizados
print("\n=== USUARIOS ACTUALIZADOS ===")
for username, datos in usuarios.items():
    print(f"@{username}: {datos['nombre']} - {datos['email']}")

