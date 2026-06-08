"""Funciones Lambda (Anónimas)
La estructura de una función Lambda es minimalista. No tiene nombre, no usa paréntesis para los parámetros y el return
está implícito:
              lambda parámetros: expresión o resultado

comparativa

¿Cuándo se utilizan en el Backend?
Se usan principalmente como "ayudantes" dentro de otras funciones nativas de Python para ordenar o limpiar datos que vienen 
de una base de datos rápidamente. """

def calcular_iva(precio):
  return precio * 0.19

##  forma lambda:
calcular_iva_lambda = lambda precio: precio * 0.19

print(calcular_iva_lambda(100))


