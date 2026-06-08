""" El simulador de saldo bancario (nonlocal)
Crearemos una función que emule una cuenta de banco protegida.
    - Requerimiento: Crar una función externa llamada
    crear_cuenta_bancaria(saldo_inicial: float):
    - Adentro de ella: Declara una función interna llamada retirar(monto: float).
    - Lógica de la función interna: Debe modificar el saldo_inicial. Si el monto a retirar es menor o igual al saldo,
    se resta del saldo y retorna el nuevo saldo. Si el monto es mayor, debe retornar un mensaje: "Fondos insuficientes".
    - Lógica final de la función externa: Debe hacer un return retirar (Devolver la función interna para poder usarla 
                                                                          como una fábrica).
    - Prueba esperada: mi_cuenta = crear_cuenta_bancaria(500)
    print(mi_cuenta(100))
    print(mi_cuenta(500)) """

def crear_cuenta_bancaria(saldo_inicial: float):
    saldo = saldo_inicial
    def retirar(monto: float):
        nonlocal saldo
        if monto <= saldo:
            saldo -= monto
            return saldo
        return "Fondos insuficientes"
    return retirar

mi_cuenta = crear_cuenta_bancaria(500)
print(mi_cuenta(100))
print(mi_cuenta(500))
