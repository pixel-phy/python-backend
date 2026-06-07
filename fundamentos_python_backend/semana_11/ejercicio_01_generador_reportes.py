"""El Generador de reportes (*args)
Imagina que estás desarrollando el sistema de logs (historial) del servidor. Necesitas una función llamada 
crear_reporte_logs que reciba un parámetro obligado llamado modulo (un str) y luego reciba una lista variable
de strings con los errores que ocurrieron.
    - Requerimiento: La función debe imprimir un encabezado con el nombre del módulo en mayúsculas y luego recorrer 
con un ciclo todos los errores recibidos en *args para listarlos.
    - Prueba esperada: 
    crear_reporte_logs("ventas", "Error 404", "Pago rechazado", "Timeout de BD") """

def crear_reporte_logs(modulo: str, *args):
    print(modulo.upper())
    for error in args:
        print(error)

crear_reporte_logs("ventas", "Error 404", "Pago rechazado", "Timeout de BD")

