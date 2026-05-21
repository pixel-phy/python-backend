"""Sistema de permisos por roles
Una API necesita gestionar permisos de usuarios según su rol. Cada rol tiene un conjunto de permisos.
Requisitos:
1. Mostrar los permisos de cada rol.
2. Verificar si el rol editor tiene permiso para "escribir".
3. Verificar si el rol admin tiene todos los permisos del editor.
4. Agregar un nuevo permiso "comentar" al rol editor.
5. Crear un nuevo rol super_admin que tenga los permisos de admin más "auditar".
6. Eliminar el permiso "eliminar" del rol admin.
7. Mostrar los permisos que tiene admin pero no editor.
8. Mostrar los permisos que tiene admin o editor pero no ambos.
9. Verificar si admin e invitado tienen algún permiso en común.
10. Mostrar el resultado final de todos los roles después de las modificaciones."""

permisos_admin = {"leer", "escribir", "eliminar", "crear", "gestionar_usuarios"}
permisos_editor = {"leer", "escribir"}
permisos_visor = {"leer"}
permisos_invitado = set()

print("\n--- PERMISOS DE CADA ROL ---")
print(f"Admin: {permisos_admin}")
print(f"Editor: {permisos_editor}")
print(f"Visor: {permisos_visor}")
print(f"Invitado: {permisos_invitado}")

# Verificamos si editor tiene permiso para "escribir"
if "escribir" in permisos_editor:
    print("\nEditor sí tiene el permiso para 'escribir'")
else:
    print("\nEditor no tiene permiso para 'escribir'")

# Admin tiene todos los permisos del editor
if permisos_admin.issuperset(permisos_editor):
    print("\nEl rol admin NO tiene todos los permisos del editor")
else:
    print("\nEl rol del editor SI tiene todos los permisos del editor.")

# Agregar nuevo permiso al rol editor
permisos_editor.add("comentar")

# Nuevo rol con permisos de admin + auditar
super_admin = permisos_admin.copy()
super_admin.add("auditar")
print(f"\nSuper admin: {super_admin}")

# Eliminar el permiso "eliminar" de admin
permisos_admin.remove("eliminar")

# Permisos que tiene admin pero no editor
diferencia = permisos_admin - permisos_editor
print(f"\nDiferencia: {diferencia}")

# Permisos de admin o editor pero no ambos
dif_simetrica = permisos_admin ^ permisos_editor
print(f"\nDiferencia simétrica: {dif_simetrica}")

# Verificar si admin e invitado tienen algún permiso en común
if permisos_admin.isdisjoint(permisos_invitado):
    print("\nRol de admin e invitado NO tienen permisos en común")
else:
    print("\nRol de admin e invitado Sí tiene permisos en común")

# Mostramos todos los roles y permisos actualizados
print("\n--- PERMISOS ACTUALIZADOS ---")
print(f"Super admin: {super_admin}")
print(f"Admin: {permisos_admin}")
print(f"Editor: {permisos_editor}")
print(f"Visor: {permisos_visor}")
print(f"Invitado: {permisos_invitado}")
