"""El decorador de Logs de Auditoría
Queremos que cada vez que un administrador ejecute una función crítica del sistema
(como borrar o cambiar configuración), quede registro en la consola que diga "Acción crítica ejecutada".
    - Requerimiento: Crear un decorador llamado registrar_auditoria.
    - Lógica interna (wrapper): Debe imprimri en consola el mensaje "LOGS: Se ha ejecutado 
    una acción en el sistema". Justo después, debe ejecutar la función original (asegúrate de 
    que el wrapper acepte *args y **kwargs y retorne el resultado de la función original).
    - Prueba esperada: Crea una función simple llamada eliminar_usuario(username) decorada con 
    @registrar_auditoria que solo imprima f"Usuario {username} eliminado". Al llamarla, deberías ver ambos mensajes. """

# Se define el decorador
def registrar_auditoria(funcion_original):
    def wrapper(*args, **kwargs):
        print("LOGS: Se ha ejecutado una acción en el sistema")
        resultado = funcion_original(*args, **kwargs)
        return resultado
    return wrapper

@registrar_auditoria
def eliminar_usuario(username):
    print(f"Usuario '{username}' eliminado.")

eliminar_usuario("Miguel01")
