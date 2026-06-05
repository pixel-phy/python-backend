""" Reto: Contador de intentos de Login

Estás programando el sistema de seguridad para el inicio de sesión de un usuario.
Queremos llevar el control de cuántos intentos fallidos lleva un usuario en el servidor,
pero el contador de intentos debe ser una variables global (para simular el estado del servidor) y la
función debe encargarse de actualizarlo localmente de forma sergura. 

1. Crea una variable global llamada INTENTOS_FALLIDOS_MAXIMOS con el valor de 3.
2. Crea otra variable global llamada contador_errores que empiece en 0.
3. Crea una función llamada intentar_login que reciba dos parámetros:
    password_correcto (el password real en la BD) y password_ingresado (lo que escribió el usuario).
4. Lógica: 
    - Si los passwords coinciden, la función debe retornar: "Acceso concedido".
    - Si no coinciden, la función debe incrementar el contador_errores en 1.
    - Ojo: Como modificar una variable global dentro de una función para poder sumarle 1.
    - Si el contador_errores llega a ser igual o mayor que INTENTOS_FALLIDOS_MAXIMOS, la función debe retornar:
    " Cuenta bloqueada por seguridad". De lo contario, debe retornar: "Password incorrecto. Intento fallido." """

INTENTOS_FALLIDOS_MAXIMOS = 3
contador_errores = 0

def intentar_login(password_correcto:str, password_ingresado:str):
    global contador_errores
    
    if contador_errores >= INTENTOS_FALLIDOS_MAXIMOS:
        return "Cuenta bloqueada por seguridad"

    if password_correcto == password_ingresado:
        return "Acceso concedido"

    else:
        contador_errores += 1

        if contador_errores >= INTENTOS_FALLIDOS_MAXIMOS:
            return "Cuenta bloqueada por seguridad"
        else:
            return "Password incorrecto. Intento fallido."


print(intentar_login("secreto123", "clave_falsa_1"))
print(intentar_login("secreto123", "clave_falsa_2"))
print(intentar_login("secreto123", "secreto123"))

# print(intentar_login("secreto123", "secreto_123"))

