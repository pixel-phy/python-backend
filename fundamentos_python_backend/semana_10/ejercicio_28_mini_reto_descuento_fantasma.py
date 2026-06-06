""" El descuento fantasma
El jefe de desarrollo quiere que la plataforma tenga un descuento global del 10% para todos los usuarios durante el Black Friday. 
El programador creó una variable global DESCUENTO_GLOBAL, pero cuando corre la función, el precio final no cambia, sigue cobrando el
precio completo.

DESCUENTO_GLOBAL = 10

def aplicar_black_friday(precio_producto:float):
    precio_final = precio_producto * (1 - DESCUENTO_GLOBAL / 100)
    return precio_final

print("Precio final (esperado 90):", aplicar_black_friday(100)) """

DESCUENTO_GLOBAL = 10

def aplicar_black_friday_vip(precio_producto: float, es_vip:bool):
    global DESCUENTO_GLOBAL

    if es_vip:
        DESCUENTO_GLOBAL = 20

    return f"{precio_producto * (1 - DESCUENTO_GLOBAL / 100):.2f}"

print(aplicar_black_friday_vip(100, False))
print(aplicar_black_friday_vip(100, True))
