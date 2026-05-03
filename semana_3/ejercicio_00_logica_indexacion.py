"""Indexación básica:
Aprender a acceder a caraceteres específicos de un string.
Dala la variable:
texto = "Python Backend" 
Utilizando [], extraer y mostrar:
1. El primer caracter.
2. El último caracter.
3. El caracter en la pocisión 7 (Empezando desde el 0)
4. El penúltimo caracter.
"""
print("\n=== INDEXACIÓN BÁSICA === \n")
# Llamamos la variable
texto = "Python Backend"
primer_caracter = texto [0]
ultimo_caracter = texto[-1]
caracter_posicion_7 = texto[7]
penultimo_caracter = texto[-2]

print("\n--- RESULTADOS ---\n")
print(f"Primer caracter: {primer_caracter}")
print(f"Último caracter: {ultimo_caracter}")
print(f"Caracter en la posición 7: {caracter_posicion_7}")
print(f"Penúltimo caracter: {penultimo_caracter}")