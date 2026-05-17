""" Tuplas anidadas:
1. Crea una tupla que contenga otras dos tuplas.
primera tupla: (1, 2, 3)
segunda tupla : (4, 5, 6)
tupla_principal: (primera, segunda)

2. Accede al número 3 desde la tupla principal.
3. Accede al número 5 desde la tupla principal.
4 Desempaqueta la tupla principal en dos variables. """

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
principal = (tupla1, tupla2)

numero_3 = principal[0][2]
print(f"Acceso al número: {numero_3}")
numero_5 = principal[1][1]
print(f"Acceso al número: {numero_5}")

x, y = principal

print(f"Donde x: {x} | Donde y: {y}")