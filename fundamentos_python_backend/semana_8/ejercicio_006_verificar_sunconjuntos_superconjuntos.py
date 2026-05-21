"""Verificar subconjuntos y superconjuntos
Útil para validar permisos, roles, etc..."""

# Ejemplo
permisos_admin = {"leer", "escribir", "eliminar", "crear"}
permisos_editor = {"leer", "escribir"}

# permisos_editor está contenido en permisos_admin
es_subconjunto = permisos_editor.issubset(permisos_admin)
print(f"¿Editor es subconjutos de admin? {es_subconjunto}")

# permisos_admin contiene a permisos_editor
es_superconjunto = permisos_admin.issuperset(permisos_admin)
print(f"Admin es superconjutno de Edito? {es_superconjunto}")

# No tienen elementos en común?
A = {1, 2, 3}
B = {4, 5, 6}
disjuntos = A.isdisjoint(B)
print(f"A y B son disjuntos: {disjuntos}")