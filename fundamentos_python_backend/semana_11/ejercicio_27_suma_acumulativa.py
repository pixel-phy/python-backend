"""Suma acumulativa (Recursión)
Imagina que en la tienda queremos calcular la suma de todos los números desde un número n hasta 1. 
    - Crear una función recursiva llamada suma_acumulativa(n:int).
    - Paso 1: Si n == 1, la función debe retornar 1 (ya que no hay más números hacia abajo que sumar)
    - Paso 2: Si no es 1, la función debe retornar el número actual n sumado a la llamada de la misma función
    pero con n - 1. """

def suma_acumulativa(n: int):
    if n == 1:
        return 1
    return n + suma_acumulativa(n - 1)

print(suma_acumulativa(4))
