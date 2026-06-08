"""El incrementador de precios por inflación (map())
Debido a la inflación de mitad de año, el backend de una tienda en línea necesita
actualizar el precio de todos los productos del catálogo sumándoles un 5% de forma masiva.

Tenemos la siguiente lista de precios puros:

    precios_antiguos = [100, 200, 500, 1000]

    Requerimiento: Utiliza la función nativa map() junto con una función lambda para crear 
    uan nueva lista llamada precios_nuevos. La lambda debe tomar cada precio y multiplicarlo
    por 1.05 (para sumarle el 5%). """

precios_antiguos = [100, 200, 500, 1000]

precios_nuevos = list(map(lambda p: round(p * 1.05, 2), precios_antiguos))

print(precios_nuevos)
