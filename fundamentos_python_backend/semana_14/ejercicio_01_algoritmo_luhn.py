"""Algoritmo de Luhn (módulo 10)

    El algoritmo de Luhn es una fórmula de suma de verificación simple que se utiliza principalmente para validar 
    números de identificación, como números de tarjetas de crédito, números IMEI de teléfonos móǘiles y 
    códigos de seguridad social en varios países.

    ¿Por qué es importante en Backend?
    - validación Temprana (Fail_fast): Nos permite rechazar peticiones con números de tarjeta falsos o mal digitados
    de forma inmediata en tu API, antes de realizar una petición HTTP costosa a una pasarela de pagos. Las pasarelas
    cobran comisiones o penalizan el exceso de peticiones fallidas.
    - Protección contra errores de tipeo: Está diseñado específicamente para detectar errores accidentales,
    como la transposición de dos dígitos adyacentes (escribir 86 en lugar de 68).
    - Eficiencia de recursos: Se ejecuta en memoria en timpo de O(n), lo que ahorra ciclos de CPU y conexiones de base de datos.

    ¿Cómo funciona el algoritmo?
    1. Se toma el número de derecha a izquierda, empezando por el penúltimo dígito.
    2. Multiplicamos por 2 cada dos digitos (es decir, posiciones impares desde la derecha:
    penúltimo, antepenúltimo del antepenúltimo, etc.).
    3. Si el resultado de la multiplicación es mayor que 9, se resta el 9 (o se suman sus dos dígitos, que da el mismo resultado).
    4. Se suman todos los digitos modificados y los no modificados.
    5. Si el total de la suma es múltiplo de 10 (termina en 0), el número es válido. """

# Ejemplo:
def es_tarjeta_valida(numero_tarjeta: str):
    # Eliminamos espacios o guiones que puedan venir del payload del request
    digitos = [int(d) for d in numero_tarjeta if d.isdigit()]

    # Si contiene caracteres no numéricos o está vacío, no es válido
    if not digitos or len(numero_tarjeta) != len([c for c in numero_tarjeta if c.isdigit() or c in "-"]):
        return False

    # Invertimos la lista para operar de derecha a izquierda fácilmente
    digitos.reverse()

    suma_total = 0
    for indice, digito in enumerate(digitos):
        if indice % 2 == 1: # Posiciones impares (empezando desde el segundo dígito)
            digito_duplicado = digito * 2
            if digito_duplicado > 9:
                digito_duplicado -= 9
            suma_total += digito_duplicado
        else:
            suma_total += digito

    return suma_total % 10 == 0

# Prueba
print(es_tarjeta_valida("49927398716"))
