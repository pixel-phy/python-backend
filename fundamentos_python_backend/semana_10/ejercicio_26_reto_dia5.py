""" Procesador de descuentos documentado
Crear una función para el sistema de facturación de un Backend, pero esta vez el foco principal es que esté 
perfectamente documentada y tipada.
Tarea: Crear una función llamada calcular_precio_final
1. Debe recibir tres parámetros con sus tipos definidos: precio_base (float), porcentaje_descuento (int) y 
cupon_valido (bool)
2. Lógica:
    - Si cupon_valido es True, se le suma un 5% extra el porcentaje de descuento que haya llegado.
    - La función debe calcular el precio final restándole el descuento total al precio base. 
    - Debe retornar el precio final como float.
3. El núcleo del reto: Debes redactar su Docstring completo debajo de la definición, explicando brevemente la función, sus argumentos (Args) con sus tipos y lo que retorna (Returns). """

def calcular_precio_final(precio_base:float, porcentaje_descuento:int= 0, cupon_valido:bool=False):
    """
    Valida el precio final de un producto según su precio_base y el uso de un cupón.
    Args:
        precio_base (float): Precio original del producto.
        porcentaje_descuento (int): Porcentaje de descuento inicial (0 - 100). Por defecto 0.
        cupon_valido (bool): Si el cupón está vigente. Si es True, añade un 5% de descuento adicional. Por defecto False.

    Returns:
        precio_final: El precio final del producto tras aplicar los descuentos. """

    if cupon_valido:
        porcentaje_descuento += 5
        
    return f"{precio_base * (1 - porcentaje_descuento/100):.2f}"

print(calcular_precio_final(100000, 50, True))
print(calcular_precio_final(100000, 25, False))
