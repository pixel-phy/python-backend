"""El Decorador de autenticación de Roles (Simulado)
En una API, no todos los usuarios pueden ejecutar todas las funciones. Necesitamos
interceptar la ejecución para verificar si el usuario tiene el rol permitido.
    - Requerimiento: Crea un decorador llamado requiere_admin.
    - Lógica interna (wrapper): El wrapper va a recibir un parámetro obligatorio llamado rol 
    (string) como primer argumento, además de los *args y kwargs correspondientes.
        - Si rol == "admin", debe ejecutar la función original y retornar su resultado.
        - Si el rol es cualquier otra cosa (como "invitado"), no debe ejecutar la función original
        y en su lugar debe retornar el string: "Acceso denegado: Se requieren permisos de administrador". """

def requiere_admin(funcion_original):
    def wrapper(*args, **kwargs):
        rol = args[0] if args else kwargs.get("rol")

        if rol == "admin":
            
            return funcion_original(*args, **kwargs)

        return "Acceso denegado: Se requieren permisos de administrador"
    return wrapper

@requiere_admin
def ver_reporte_financiero(rol):
    return "--- Datos Financieros Confidenciales de la Empresa ---"

print(ver_reporte_financiero("invitado"))
print(ver_reporte_financiero("admin"))
