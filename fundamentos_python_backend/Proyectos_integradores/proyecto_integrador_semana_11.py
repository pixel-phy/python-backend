"""E-Commerce Core 
Bloque 1: Sistema de logs seguros (decoradores)
Cada vez que un usuario intenta realizar una acción crítica (comprar y obtener descuento)
el sistema debe registrar en la consola qué función se ejecutó y con qué argumentos, para 
poder rastrear posibles hackeos.
- Crear un decorador llamado auditar_accion.
- Wrapper: Debe recibir los parámetros normales.
    - Primero debe imprimir en consola: f"[AUDITORIA] Ejecutando la función: {funcion_original.__name__}".
     (Nota: __name__ es un truco de python que da la función en texto).
    - Segundo: debe imprimir los argumentos recibidos: f"[DATOS]: posicionales={args}, Nombrador={kwargs}".
    - Debe ejecutar la función original con sus bolsas intactas y retornar su resultado. 

Bloque 2: El motor de impuestos avanzado (funciones lambda)
Crear un diccionario llamado motores_impuestos.
Contenido del diccionario: Debe tener tres llaves (países) y su valor debe ser una función 
lambda que reciba un parámetro subtotal:
    - "CO" (Colomnia): Debe calcular el 19% del subtotal (subtotal x 0.19).
    - "MX" (México): Debe calcular el 16% del subtotal (subtotal x 0.16).
    - "USA" (Estados Unidos): Debe calcular el 7% del subtotal (subtotal x 0.07). 

Bloque 3: El contador de envíos VIP (Ámbitos y nonlocal)
La tienda tiene una regla: los primeros 3 envíos de un usuario VIP son completamente gratis.
Después del tercer envío, se empieza a coobrar una tarifa fija. Necesitamos blindar este contador en el
backend usando un closure para que nadie pueda resetear el contador desde afuera.
    - Crear una función externa llamada crear_despachador_vip().
    - Adentro, inicializar contador_envios.
    - Crear una función interna generar_envio().
        - Debe usar nonlocal para poder modificar contador_envios.
        - Cada vez que se ejecute, debe sumar 1 al contador_envios.
        Lógica del cobro:
            - Si contador_envios <= 3, debe retornar: f"Envío #{contador_envios} generado. 
            ¡Costo: $0.00 (Beneficio VIP)!"
            - Si contador_envios > 3, debe retornar: f"Envío #{contador_envios} generado. Costo: $10.00."
    - Lógica final: Retornar la función interna generar_envio.

Bloque 4: El procesador de descuentos en Cascada (Recursión)
Un cliente tiene una lista de porcentajes de descuento que se deben apllicar uno tras otro al precio de su 
producto. Por ejemplo, si el producto vale $100 y la lista de descuentos es [10, 20], primero se aplica el 
10% y louego se aplica el 20%.
    - Crear una función llamada aplicar_descuentos_recursivos(precio, lista_descuentos)
    - Paso 1: Si la lista_descuentos está vacía, significa que ya no quedan más descuentos por aplicar. 
    La función debe retornar precio actual.
    - Paso 2: Si la lista tiene elementos:
        1. Extrae el primer descuento de la lista.
        2. Calcula el nuevo precio aplicando ese descuento.
        3. Retorna la ejecución de la misma función, pero pasándole el nuevo_precio y la lista_descuentos.
"""
# Bloque 1:

def auditar_accion(funcion_original):
    def wrapper(*args, **kwargs):
        print(f"[AUDITORIA]: {funcion_original.__name__}")
        print(f"[DATOS]: posicionales={args}, Nombrador={kwargs}")
        return funcion_original(*args, **kwargs)
    return wrapper

@auditar_accion
def procesar_pago(usuario: str, total: float):
    return f"Pago de ${total} procesado para el usuario {usuario}."

@auditar_accion
def aplicar_cupon(codigo: str, porcentaje: int):
    return f"Cupón {codigo} del {porcentaje}% activado."

print(procesar_pago("Miguel", 250.0))
print(aplicar_cupon("DESCUENTOXD", 30))

# Bloque 2:

motores_impuesto = {"CO": lambda subtotal: subtotal * 0.19, 
                    "MX": lambda subtotal: subtotal * 0.16, 
                    "USA": lambda subtotal: subtotal * 0.07
                    }

print(f"{motores_impuesto["CO"](100.0):.2f}")
print(f"{motores_impuesto["MX"](100.0):.2f}")
print(f"{motores_impuesto["USA"](100.0):.2f}")

# Bloque 3:

def crear_despachador_vip():
    contador_envios = 0
    def generar_envio():
        nonlocal contador_envios
        contador_envios += 1
        if contador_envios <= 3:
            return f"Envío #{contador_envios} generado. ¡Costo: $0.00 (Beneficio VIP)!"
        return f"Envío #{contador_envios} generado. Costo: $10.00."
    return generar_envio

despachar = crear_despachador_vip()
print(despachar())
print(despachar())
print(despachar())
print(despachar())
print(despachar())

# Bloque 4:

def aplicar_descuentos_recursivos(precio: float, lista_descuentos: list):
    if not lista_descuentos:
        return precio
    descuento = lista_descuentos.pop(0)
    nuevo_precio = precio * (1 - descuento / 100)
    return aplicar_descuentos_recursivos(nuevo_precio, lista_descuentos)

precio_inicial = 100.0
descuentos = [10, 20]
precio_final = aplicar_descuentos_recursivos(precio_inicial, descuentos)
print(f"Precio final con descuentos aplicados: ${precio_final:.2f}")
