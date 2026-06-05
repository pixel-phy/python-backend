""" Retorno de valores (Simple, múltiple y temprano)

En Backend manejamos tres formas de retorno de datos:
    1. Retorno simple:
    Regresa un solo dato (string, número, diccionario).
    2. Retorno múltiple (varios datos).
    3. Retorno temprano """

# Retorno simple
return "ok"

# Retorno múltiple
def obtener_metricas():
    usuarios = 150
    ventas = 3000.50
    return usuarios, ventas
cant_usuarios, total_ventas = obtener_metricas()

# Retorno temprano
def procesar_pago(monto):
    if monto <= 0:
        return "Error: Monto inválido" # Retorno temprano 1
    if no_hay_internet():
        return "Error: Sin conexión"

    # Si todo está bien
    ejecutar_transaccion(monto)
    return "Pago exitoso"
