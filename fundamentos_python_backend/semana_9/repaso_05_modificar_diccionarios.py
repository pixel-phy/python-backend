"""Modificar y agregar elementos
En Backend es muy común actualizar diccionarios dinámicamente."""

# Diccionario inicial
sesion_usuario = {
    "id": 123,
    "nombre": "Ana"
}

# Agregar nueva clave-valor
sesion_usuario["autenticado"] = True

# Modificar valor existente
sesion_usuario["nombre"] = "Ana López"

# Verificar si existe una clave antes de usarla
if "email" not in sesion_usuario:
    sesion_usuario["email"] = "ana@mail.com"

print(sesion_usuario)


