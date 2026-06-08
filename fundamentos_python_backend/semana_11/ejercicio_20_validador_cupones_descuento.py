"""El validador de cupones de descuento
Imagina que tienes una función en tu pasarela de pagos que aplica un descuento al total de la compra.
Queremos un decorador que valide si el cupón que ingresó el usuario es válido antes de aplicar el 
descuento. 
    - Requerimiento: Crea un decorador llamado validar_cupon.
    - Lógica interna (wrapper): El wrapper debe recibir el parámetro codigo_cupon (string).
        - Si codigo_cupon == "DESCUENTO20", debe dejar pasar la ejecución retornando
        funcion_original(codigo_cupon).
        - Si el código es cualquier otra cosa, el decorador debe frenar la función y retornar 
        el string: "Cupón inválido o expirado". """

def validar_cupon(funcion_original):
    def wrapper(codigo_cupon: str):
        if codigo_cupon == "DESCUENTO20":
            return funcion_original(codigo_cupon)
        return "Cupón inválido o expirado"
    return wrapper

@validar_cupon
def aplicar_descuento(codigo_cupon):
    return "¡Éxito! Se ha aplicado un 20% de descuento a tu carrito."

print(aplicar_descuento("FALSO10"))
print(aplicar_descuento("DESCUENTO20"))
