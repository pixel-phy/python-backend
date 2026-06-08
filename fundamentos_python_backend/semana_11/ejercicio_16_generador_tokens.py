"""El generador de tokens/IDs únicos
En el Backend cuando creas usuarios o tareas, a veces necesitas un contador interno que genere un identificador
único (ID1, ID2, ID3...) de forma incremental cada vez que se registra algo.

    - Requerimiento: Crear una función externa llamada generador_ids(). Adentro, declara una variable contador = 0.
    - Función interna: Crea una función interna llamada siguiente_id(). Debe usar nonlocal para incrementar el contador 
    en 1 cada vez que se llame, y retornar el nuevo valor del contador. 
    - Lógica final externa: Retorna la función interna siguiente_id.
    - Prueba esperada:
        nuevo_id = generador_ids()
        print(nuevo_id())
        print(nuevo_id())
        print(nuevo_id())
        print(nuevo_id()) """

def generador_ids():
    contador = 0
    def siguiente_id():
        nonlocal contador
        contador += 1 
        return contador
    return siguiente_id

nuevo_id = generador_ids()
print(nuevo_id())
print(nuevo_id())
print(nuevo_id())
