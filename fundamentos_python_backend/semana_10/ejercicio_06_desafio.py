"""Crear una función validar_usuario(usuario) que verifique:
    - El usuario tiene entre 3 y 20 caracteres.
    - Solo contiene letras, números y guión bajo _
    - No está vacío

Retorna True si cumple todo, False en caso contrario"""

def validar_usuario(usuario):
    if not(3 <= len(usuario) <= 20): 
        return False
    if not usuario:
        return False
    for caracter in usuario:
        if not(caracter.isalnum() or caracter == "_"):
            return False
    
    return True

print(validar_usuario("carlos_dev"))
print(validar_usuario("jo"))
print(validar_usuario("usuario#123"))

