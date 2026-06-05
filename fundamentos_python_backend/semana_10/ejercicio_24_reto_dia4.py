"""Validador de registro con "Early return"
Aplicaremos retorno temprano y retorno múltiple para programar una función que procese el formulario de registro
de nuevos usuarios en una plataforma.

Crear una función llamada validar_y_crear_usuario.
1. Debe recibir tres parámetros: username, email y password.
2. Lógica en retorno temprano:
    - Si el username tiene menos de 4 caracteres, debe retornar inmediatamente: (False, "El nombre de usuario es muy corto").
    - Si el email no contiene un @, debe retornar inmediatamente (False, "El email no es válido")
    - Si el password tiene menos de 6 caracteres, debe retornar inmediatamente: (False, "La contraseña es insegura").
3. Si pasa todas las validaciones (llega al final de la función), debe crear un diccionario simulado el usuario guardado y retornar:
    (True, {"username": username, "email": email, "activo": True}). """

def validar_y_crear_usuario(username:str, email:str, password:str):
    if len(username) < 4:
        activo = False
        mensaje = "El nombre de usuario es muy corto"
        return (activo, mensaje)
    if "@" not in email:
        activo = False
        mensaje = "El email no es válido"
        return (activo, mensaje)
    if len(password) < 6:
        activo = False
        mensaje = "La contraseña es insegura"
        return (activo, mensaje)
    activo = True
    datos = {
            "username": username,
            "email": email,
            "activo": activo
            }
    return (activo, datos)

print(validar_y_crear_usuario("mig", "miguel@mail.com", "secreto1234"))
print(validar_y_crear_usuario("Migue07", "miguel.com", "secreto1234"))
print(validar_y_crear_usuario("Migue007", "miguel@mail.com", "sec1"))
print(validar_y_crear_usuario("Miguel007", "miguel@mail.com", "secreto1234"))

