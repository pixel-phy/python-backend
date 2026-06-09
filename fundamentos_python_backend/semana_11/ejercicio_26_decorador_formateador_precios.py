""" El decorador "Formateador de precios"
    En nuestro Backend de e-commerce, a veces los números flotantes sse ven feos.
    Queremos un decorador que convierta el resultado numérico de una función en un string
    bonito con el signo de dólar y dos decimales.
    - Crear un decorador llamado formatear_moneda.
    - Lógica del wrapper: No recibe parámetros propios, solo intercepta la función original.
    Debe guardar el resultado de la función original en una variable. Luego, debe retornar ese 
    valor formateado. """

def formatear_moneda(funcion_original):
    def wrapper(*args, **kwargs):
        resultado = funcion_original(*args, **kwargs)
        return f"${resultado:.2f}"
    return wrapper

@formatear_moneda
def calcular_iva(precio_base):
    return precio_base * 0.19

print(calcular_iva(100))
