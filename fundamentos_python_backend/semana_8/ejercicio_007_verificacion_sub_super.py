"""Hacer lo mismo que en el ejercicio anterior"""

usuario_verificados = {"Ana", "Luis", "Carlos"}
usuarios_activos = {"Ana", "Luis", "Carlos", "Sofía", "Juan"}

# ¿Todos los usuarios verificados están activos?
son_subsets = usuario_verificados.issubset(usuarios_activos)
print(f"Todos los usuarios verificados están activos: {son_subsets}")

# ¿Los usuarios activos cotienen a todos los verificados?
es_superset = usuarios_activos.issuperset(usuario_verificados)
print(f"Los usuarios activos contienen a todos los verificados: {es_superset}")

usuarios_admin = {"Ana"}
es_subconjunto = usuarios_admin.issubset(usuario_verificados)
print(f"Los usuarios admin son subconjunto de los verificados: {es_subconjunto}")