"""El calculador de impuestos en lote:
En los sistemas de facturación, a veces hay que aplicar un impuesto fijo a una lista 
variable de precios de productos que el usuario tiene en el carrito.
  - Requerimiento: Crea una función llamada aplicar_impuesto_lote. Debe recibir un 
    parámetro obligatorio llamado porcentaje_impuesto (int). Después debe recibir una
    cantidad variable de precios usando *args.

  - Lógica: La función debe calcular el precio final con impuesto para cada uno de los 
    números que vengan en *args y retornar una lista con los nuevos precios redondeados
    a 2 decimales.

  - Prueba esperada: print(aplicar_impuesto_lote(19, 100, 250, 50)) """

def aplicar_impuesto_lote(porcentaje_impuesto: int, *args):
  lista_impuestos = []
  for lote in args:
    lista_impuestos.append(round(lote * (1 + porcentaje_impuesto/100), 2))
  return lista_impuestos

print(aplicar_impuesto_lote(19, 100, 250, 50))
  
