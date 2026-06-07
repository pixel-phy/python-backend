"""Administrar usuarios en la memoria del servidor 
Se programarán tres funciones que interactúan con una base de datos simulada. registrar_usuario(username: str, email: str):
    - Regla 1 (Retorno temprano): Si el username ya existe en las llaves de SISTEMA_USUARIOS, debe retornar inmediatamente
    un diccionario de error: {"status": "error", "message": "EL usuario ya existe"}.
    - Regla 2 (Retorno temprano): Si el email no contiene un @, debe retornar, {"status": "error", "message": "Email inválido"}
    - Caso exitoso: Si para las reglas, debe agregar el nuevo usuario al diccionario global SISTEMA_USUARIOS.
    Por defecto, todos los usuarios nuevos se registran con el plan "free" y el estado activo: true. Al final, retorna un
    diccionario con "status": "success" y el mensaje "Usuario registrado con éxito".
cambiar_plan(username: str, nuevo_plan: str)
    - Regla 1 (Retorno temprano): Si el username no existe en la base de datos, debe retornar un diccionario con "status": "error"
    y el mensaje "Usuario no encontrado".
               - Regla 2 (Retorno temprano): Los únicos planes válidos en tu empresa son "free" y "premium". Si te pasa otro plan
    retorna un error: "Plan no reconocido".
    - Caso exitoso: Si todo está bien, actualiza el campo "plan" de ese usuario específico dentro del diccionario global y retorna
    un estatus de "success".
obtener_usuarios_activos():
    - Esta función no recibe parámetros. Debe recorrer el diccionario global, filtrar y retornar una lista que contenga únicamente
    los username de los usuarios que tengan "activo": True. """

SISTEMA_USUARIOS = {
    "miguel01": {"email": "miguel@mail.com", "plan": "free", "activo": True},
    "ana77": {"email": "ana@mail.com", "plan": "premium", "activo": False}
}

def registrar_usuario(username: str, email: str):
    global SISTEMA_USUARIOS

    if username in SISTEMA_USUARIOS:
        return {"status": "error", "message": "El usuario ya existe"}
    
    if not "@" in email:
        return {"status": "error", "messasge": "Email inválido"}

    SISTEMA_USUARIOS[username] = {
        "email": email, 
        "plan": "free", 
        "activo": True
    }
    return {"status": "success", "message": "Usuario registrado con éxito"}

def cambiar_plan(username: str, nuevo_plan: str):
    global SISTEMA_USUARIOS
    planes = ["free", "premium"]

    if not username in SISTEMA_USUARIOS:
        return {"status": "error", "message": "Usuario no encontrado"}

    if nuevo_plan not in planes:
        return {"status": "error", "message": "Plan no reconocido"}

    SISTEMA_USUARIOS[username]["plan"] = nuevo_plan
    return {"status": "success", "message": f"Plan actualizado a {nuevo_plan}"}

def obtener_usuarios_activos():
    usuarios_activos = []

    for clave, valor in SISTEMA_USUARIOS.items():
        if valor["activo"] is True:
            usuarios_activos.append(clave)

    return usuarios_activos

print("Intento registrar usuario repetido")
print(registrar_usuario("miguel01", "otro_correo@mail.com"))

print("\nRegistrando nuevo usuario 'carlos99'")
print(registrar_usuario("carlos99", "carlos@mail.com"))

print("\nCambiando el plan de 'miguel01' a premium")
print(cambiar_plan("miguel01", "premium"))

print("\nListando todos los usuarios activos en el sistema")
print("Usuarios activos actualmente:", obtener_usuarios_activos())
