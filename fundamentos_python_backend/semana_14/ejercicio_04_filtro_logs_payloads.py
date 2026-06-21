""" Ejercicio 04: Filtro de Logs de Payloads Corruptos

    En una arquitectura de microservicios, recibes un lote (una lista de strings) con peticiones
    de pago. Algunas tarjetas vienen con caracteres basura por errores de codificación. Crear
    una función filtrar_pagos_validos(batch: list[str]) -> dict. Debe procesar la lista y retornar 
    un diccionario con este formato exacto:
        {
        "validos": ["tarjeta1", "tarjeta2"],
        "invalidos": ["tarjeta3"],
        "corruptos": ["tarjeta_con_letras_o_vacia"]
    }
"""
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

def filtrar_pagos_validos(batch: list[str]) -> dict:
    # Inicializar el diccionario de resultados
    resultado = {
        "validos": [],
        "invalidos": [],
        "corruptos": []
    }

    # Procesar cada elemento del batch
    for tarjeta in batch:
        # Limpiar la tarjeta para verificar si está corrupta
        tajeta_limpia = tarjeta.replace(" ", "").replace("-", "")

        # Verificar si es corrupta (contiene letras o está vacía)
        if not tajeta_limpia or not tajeta_limpia.isdigit():
            resultado["corruptos"].append(tarjeta)
        else:
            # Si no está corrupta, validar luhn
            if validar_luhn(tarjeta):
                resultado["validos"].append(tarjeta)
            else:
                resultado["invalidos"].append(tarjeta)

    return resultado

# Lista de prueba con diferentes casos
batch_pagos = [
    "4539 1488 0343 6467",
    "4539-1488-0343-6467",
    "4539 1488 0343 6468",
    "1234 5678 9012 3456",
    "4111 1111 1111 1111",
    "abc123",
    "   ",
    "49927398716",
    "",
    "12345 67890 12345",
    "4532 8776 5432 1234",
    "5555 5555 5555 4444",
]

# Ejecutar el filtro
resultado = filtrar_pagos_validos(batch_pagos)

# Mostrar resultados
print("=== Resultados del Filtro ===")
print(f"Válidos ({len(resultado['validos'])}):")
for tarjeta in resultado['validos']:
    print(f"  - {tarjeta}")

print(f"\nInválidos ({len(resultado['invalidos'])}):")
for tarjeta in resultado['invalidos']:
    print(f"  - {tarjeta}")

print(f"\nCorruptos ({len(resultado['corruptos'])}):")
for tarjeta in resultado['corruptos']:
    print(f"  - '{tarjeta}'")
