"""Sistema de permisos por roles
Una API necesita gestionar permisos de usuario. 
admin = {"leer", "escribir", "eliminar", "crear"}
editor = {"leer", "escribir"}
visor = {"leer"}

usuarios = ["ana", "luis", "carlos", "sofia"]
roles_usuarios = ["admin", "editor", "visor", "editor"]


1. Mostrar los permisos de cada usuario (según su rol).
2. Verificar si el usuario "ana" (admin) tiene el permiso "eliminar".
3. Crear un nuevo rol supervisor con permisos {"leer", "comentar", "moderar"}.
4. Cambiar el rol del usuario "carlos" de "visor" a "supervisor".
5. Mostrar los permisos actualizados de "carlos".
6. Agregar el permiso "auditar" al rol admin.
7. Eliminar el permiso "crear" del rol admin.
8. Mostrar los permisos finales de todos los usuarios.
9. Encontrar los permisos que tiene admin pero editor.
10. Encontrar los permisos comunes entre admin y supervisor."""

admin = {"leer", "escribir", "eliminar", "crear"}
editor = {"leer", "escribir"}
visor = {"leer"}

usuarios = ["ana", "luis", "carlos", "sofia"]
roles_usuarios = ["admin", "editor", "visor", "editor"]

print("\n--- PERMISOS POR USUARIO ---")
for i in range(len(usuarios)):
    usuario = usuarios[i]
    rol = roles_usuarios[i]

    if rol == "admin":
        permisos = admin
    elif rol == "editor":
        permisos = editor
    elif rol == "visor":
        permisos = visor

    print(f"{usuario} ({rol}): {permisos}")

if "eliminar" in admin:
    print("Ana (admin) SI puede el permiso 'eliminar'")
else:
    print("Ana (admin) NO tiene el perimos 'eliminar'")

print("\n... creando nuevo rol 'supervisor'")
supervisor = {"leer", "comentar", "moderar"}
print("... realizando cambio de rol a Carlos")
for i in range(len(usuarios)):
    if usuarios[i] == "carlos":
        roles_usuarios[i] = "supervisor"
        break

admin.add("auditar")
admin.discard("crear")
print("\n--- PERMISOS FINALES DE USUARIO ---")
for i in range(len(usuarios)):
    usuario = usuarios[i]
    rol = roles_usuarios[i]

    if rol == "admin":
        permisos = admin
    elif rol == "editor":
        permisos = editor
    elif rol == "visor":
        permisos = visor
    elif rol == "supervisor":
        permisos = supervisor

    print(f"{usuario} ({rol}): {permisos}")

print("\n--- PERMISOS QUE TIENE ADMIN PERO NO EDITOR ---")
admin_editor = admin - editor
print(admin_editor)
print("\n--- PERMISOS COMUNES ENTRE ADMIN Y SUPERVISOR ---")
comunes = admin & supervisor
print(comunes)