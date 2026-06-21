"""Ejercicio 02: El validador estricto 

Crea una función llamada validar_luhn(cadena_numerica: str). Debe recibir un string
(que puede contener espacios o guiones) y retorna si pasa o no el algoritmo.
Asegúrate de retornar False inmediatamente si la cadena contiene letras o si está vacía. """

def validar_luhn(cadena_numerica: str) -> bool:
    #Aliminar espacios y guiones
    cadena_limpia = cadena_numerica.replace(" ", ""). replace("-", "")

    #Verificar si está vacía o contiene caracteres no numéricos
    if not cadena_limpia or not cadena_limpia.isdigit():
        return False
    
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

# Pruebas
print(validar_luhn("4539 1488 0343 6467"))
print(validar_luhn("4539-1488-0343-6467"))
print(validar_luhn("4539 1488 0343 6468"))
print(validar_luhn("abc123"))
print(validar_luhn(""))
print(validar_luhn("   "))
