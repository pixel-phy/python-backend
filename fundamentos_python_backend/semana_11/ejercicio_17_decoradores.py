"""Decoradores (@decorador)
En el desarrollo Backend, un decorador es simplemente una función que toma otra función como 
entrada, le añade superpoderes (lógica extra) antes o después de que se ejecute, y devuelve
la función modificada sin alterar su código original.

Se usan mucho para:
    - Verificar si un usuario está logueado antes de entrar a una ruta.
    - Medir cuánto tiempo tarda una función en responder (auditoría).
    - Guardar registros en un archivo de texto cada vez que alguien ejecuta una acción importante.

La estructura de un decorador:
    Un decorador siempre tiene tres niveles:
    - Función externa (el decorador en sí).
    - Función interna (el wrapper o envoltorio que añade los superpoderes y recibe los *args y kwargs
                        de la función original).
    - Función original (que se ejecuta adentro). """

# Por ejemplo:

# Se define el decorador:
def mi_decorador(funcion_original):
    def warpper(*args, **kwargs):
        print("Alerta! Se va a ejecutar una función...")
        resultado = funcion_original(*args, **kwargs) # Se ejecuta la función real
        print("Listo! Función ejecutada con éxito.")
        return resultado
    return warpper

# Se aplica usando el símbolo '@':
@mi_decorador
def procesar_pago(monto):
    print(f"Procesando el pago de ${monto} en la pasarela...")

# Se prueba
procesar_pago(150)
