"""La cuenta regresiva del Servidor (Recursión)
Cuando el servidor de nuestra tienda se va a reiniciar por actualizaciones,
necesitamos una función que imprima una cuenta regresiva en la consola. ¡Pero ojo, 
está prohibido usar bucles for o while! Debes lograrlo usando recursión.
    - Crear una función llamada cuenta_regresiva(numero: int).
    - Paso 1: Si el numero es igual a 0, la función debe imprimir 
    "¡Servidor Reiniciado" y cerrarse usando un return vacío.
    - Paso 2: Si no es cero, la función debe imprimir el número actual en consola.
    - Paso 3: Al final, la función debe llamarse a sí misma, pero pasándose como argumento numero - 1. """

def cuenta_regresiva(numero: int):
    if numero == 0:
        print("¡Servidor Reiniciado")
        return
    print(numero)
    return cuenta_regresiva(numero - 1)

cuenta_regresiva(3)
