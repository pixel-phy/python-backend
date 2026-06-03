"""Contador sin global
Crea una función contador_personal() que retorne otra función que cada vez que se llama incrementa un contador interno """

def contador_personal():
    contador = 0

    def incrementar():
        nonlocal contador
        contador += 1
        return contador
    return incrementar

contar = contador_personal()
print(contar())
print(contar())
print(contar())
