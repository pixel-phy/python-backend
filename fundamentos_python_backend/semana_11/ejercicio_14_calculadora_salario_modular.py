"""Calculadora de Salario Modular (encapsulamiento)
Queremos una función principal que calcule el salario neto de un empleado. Para no tener un código gigante,
meteremos una función interna encargada únicamente de calcular los descuentos de salud. 
    - Requerimientos: Crea una función externa llamada calcular_salario_neto(salario_base: float)
    - Adentro de ella: Crear una función interna llamada calcular_descuentos(). Esta función 
    interna simplemente debe tomar el salario_base de la función externa, multiplicarlo por 0.08
    y retornar ese valor del descuento.
    - Lógica final de la función externa: Debe llamar a la función interna para obtener el descuento, 
    restárselo al salario_base y retornar el salario neto final.
    - Prueba esperada: print(calcular_salario_neto(2000.0)) """

def calcular_salario_neto(salario_base: float):
    def calcular_descuentos():
        return salario_base * 0.08

descuento_total = calcular_descuentos()

    return salario_base - descuento_total 

print(calcular_salario_neto(2000.0))
