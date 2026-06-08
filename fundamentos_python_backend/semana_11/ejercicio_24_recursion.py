"""Recursión
Una función recursiva es como un ciclo while, pero en lugar de usar un bucle, 
la función se vuelve a ejecutar a sí misma con un dato más pequeño, hasta que 
llega a un "caso base" (un freno) para no congelar la computadora. """

# Por ejemplo:
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(4))
