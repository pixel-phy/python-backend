"""El convertidos de moneda Express
Muchos e-commerce muestran los precios en la moneda loca, pero internamente el backend
procesa todo en dólares.
    - Requerimientos: Crea una función lambda llamada convertir_a_dolares. Debe recibir un parámetro (precio_cop)
    y dividirlo por la tasa de cambio (asumamos $4000 para el ejercicio). El resultado debe retornar el precio en dólares.
    - Prueba esperada: print(convertir_a_dolares(40000)) (debería imprimir 10.0)"""

convertir_a_dolares = lambda precio_cop: precio_cop/4000
print(convertir_a_dolares(40000))
