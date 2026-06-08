"""El validador de cupones Exclusivos (Decoradores + Lógica)
En nuestra tienda, queremos proteger las funciones que aplican descuentos VIP. Necesitamos un
decocrador que verifique si el cupón ingresado por el comprador es un cupón válido del sistema.
    - Crear un decorador llamado requiere_cupon_valido.
    - Lógica del wrapper: debe recibir el parámetro cupon(str).
        - Si el cupon es igual a "PROMO2026", debe permitir que la función original se ejecute normalmente.
        - Si el cupon es cualquier otra cosa, debe frenar la ejecuión y retornar: "Error: El cupón ingresado no existe."
    - Funcion a decorar: Crea una función llamada procesar_descuento(cupon) que simplemente retorne: "¡Descuento del 20% aplicado con éxito!".
    - Probar código con "FALSO" y con "PROMO2026". """

def requiere_cupon_valido(funcion_original):
    def wrapper(cupon:str):
        if cupon == "PROMO2026":
            return funcion_original(cupon)
        return "Error: El cupón ingresado no existe."
    return wrapper

@requiere_cupon_valido
def procesar_descuento(cupon):
    return "¡Descuento del 20% aplicado con éxito!"

print(procesar_descuento("FALSO"))
print(procesar_descuento("PROMO2026"))
