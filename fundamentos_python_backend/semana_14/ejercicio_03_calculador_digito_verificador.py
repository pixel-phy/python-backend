"""Ejercicio 03: El calculador del digito verificador

    A veces en el Backend generamos identificadores intermitentes (como números de cuenta internos)
    y necesitamos calcular el último digito (el dígito verificador) para que toda la cadena cumpla con
    Luhn.
    Crea una función calcular_digito_luhn(numero_parcial: str) -> int. Si recibe "4992739871", la función debe calcular
    matemáticamente que el dígito que falta al final es un 6. """

def validar_luhn(cadena_numerica: str) -> bool:
    # Limpiar cadena
    cadena_limpia = cadena_numerica.replace(" ", "").replace("-", "")

    # Validaciones tempranas
    if not cadena_limpia or not cadena_limpia.isdigit():
        return False

    #Algoritmo de Luhn
    suma = 0
    # reversed() no duplica la cadena en memoria, genera un iterador de atrás hacia adelante
    for i, caracter in enumerate(reversed(cadena_limpia)):
        digito = int(caracter)
        if i % 2 == 1:
            doble = digito * 2
            suma += doble - 9 if doble > 9 else doble
        else:
            suma += digito

    return suma % 10 == 0

def calcular_digito_luhn(numero_parcial: str) -> int:
    # Limpiar cadena (espacios y guiones)
    numero_limpio = numero_parcial.replace(" ", "").replace("-", "")

    # Validar que solo tenga digitos y no esté vacío
    if not numero_limpio or not numero_limpio.isdigit():
        raise ValueError("El número parcial dede contener solo digitos")

    # Probar digitos del 0 al 9 para encontrar el verificador
    for digito in range(10):
        # Construir el número completo con el dígito candidato al final
        numero_completo = numero_limpio + str(digito)

        #Verificar si pasa el algoritmo de Luhn
        if validar_luhn(numero_completo):
            return digito

    raise ValueError("No se pudo calcular el digito verificador")

print(calcular_digito_luhn("4992739871"))
