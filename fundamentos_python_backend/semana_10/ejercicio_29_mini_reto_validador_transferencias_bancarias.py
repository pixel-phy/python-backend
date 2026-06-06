"""Validador de transferencias bancarias
Estás programando el módulo de transacciones de una billetera (Nequi, Daviplata). Cuando un usuario quiere enviarle plata a otra persona, 
el backend debe validar tres reglas estrictas antes de aprobar el movimiento.

Tarea: Crear una función llamada procesar_transferencia.
1. Debe recibir tres parámetros obligatorios:
    - saldo_actual
    - monto_a_enviar
    - cuenta_activa

2. Lógica con retorno temprano:
    - Regla 1: Si la cuenta_activa es False, la función debe cortar de inmediato y retornar un string que diga:
    "Error: La cuenta de destino está inactiva".
    - Regla 2: Si el monto_a_enviar es menor o igual a 0, debe cortar de inmediato y retornar: "Error: El monto debe ser mayor a cero".
    - Regla 3: Si el monto_a_enviar es mayor que el saldo_actual, debe cortar de inmediato y retornar: "Error: Fondos insuficientes".

3. Caso exitoso: Si pasa las tres reglas, significa que todo está perfecto. La función debe restar el monto al saldo actual y 
retornar el nuevo saldo redondeado a 2 décimales. """

def procesar_transferencia(saldo_actual: float, monto_a_enviar: float, cuenta_activa: bool):
    """ Función que realiza transferencia de cuentas bancarias si cumple con los parámetros estándares de envío, como lo son: contar con 
    fondos suficientes y cuenta de transferencia activa.

    Args: saldo_actual (float): dinero que contiene la cuenta.
    - monto_a_enviar (float): dinero que se desea enviar.
    - cuenta_activa (bool): Valida si la cuenta de destino está activa.

    Returns: 
    - Si la cuenta no está activa se retorna mensaje de error informando que la cuenta está inactiva.
    - Si el monto a enviar es menor o igual a 0, se retorna un mensaje de error diciendo que el monto debe ser mayor que cero.
    - Si el monto a enviar es mayor al saldo de la cuenta, se retorna un mensaje informando que los fondos son insuficientes.
    - Si cumple los requisitos se retorna el nuevo saldo redondeado a 2 decimales.
    """

    if not cuenta_activa:
        return "Error: La cuenta de destino está inactiva"
    if monto_a_enviar <= 0:
        return "Error: El monto debe ser mayor a 0"
    if monto_a_enviar > saldo_actual:
        return "Error fondos insuficientes"
   
    saldo_actual = saldo_actual - monto_a_enviar
    return f"{saldo_actual:.2f}"

print(procesar_transferencia(saldo_actual=50000.0, monto_a_enviar=10000.0, cuenta_activa=False))
print(procesar_transferencia(saldo_actual=5000.0, monto_a_enviar=20000.0, cuenta_activa=True))
print(procesar_transferencia(saldo_actual=50000.0, monto_a_enviar=10000.0, cuenta_activa=True))
