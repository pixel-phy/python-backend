"""El interruptor de Mantenimiento del Servidor
A veces, los administradores de un sistema necesitan poner una ruta o una función en 
"Modo Mantenimiento" para que ningún usuario pueda usarla mientras hacen reparaciones. 
Vamos a simular esto con una variable booleana.
    - Requerimiento: Crea un decorador llamado verificar_mantenimiento.
    - Lógica interna(wrapper): El wrapper va a recibir el parámetro en_mantenimiento (un booleano True o False).
        - Si en_mantenimiento == True, debe frenar la ejecución y retornar: "Servidor en mantenimiento. Inténtalo más tarde".
        - Si en_mantenimiento == False, debe permitir que la función original corra normalmente retornando funcion_original(en_mantenimiento). """

def verificar_mantenimiento(funcion_original):
    def wrapper(en_mantenimiento: bool):
        if en_mantenimiento == True:
            return "Servidor en mantenimiento. Inténtalo más tarde."
        return funcion_original(en_mantenimiento)
    return wrapper

@verificar_mantenimiento
def obtener_perfil_usuario(en_mantenimiento):
    return "--- Datos del perfil del usuario de la base de datos ---"

print(obtener_perfil_usuario(True))
print(obtener_perfil_usuario(False))

