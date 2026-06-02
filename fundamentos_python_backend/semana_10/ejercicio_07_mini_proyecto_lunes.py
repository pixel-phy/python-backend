"""Mini proyecto del día 1
Validador de emial mejorado para backend
Crear una función validar_email_backend(email) que:
    1. Verifique que tenga exactamente un @.
    2. Verifique que el dominio tenga un punto después del @.
    3. Verifique que el usuario antes del @ no esté vacío.
    4. Verifique que el dominio después del @ tenga al menos 3 caracteres """

def validar_email_backend(email):
    if '@' not in email:
        mensaje = "email sin '@'"
        return (False, mensaje)
    
    posicion = email.find("@")

    if "." not in email[posicion:]:
        return (False, "Sin . después del '@'")
    
    if not email[:posicion]:
        return (False, "Usuario vacío antes del '@'")
    
    if not len(email[posicion:]) >= 3:
        return (False, "El dominio no tiene más de tres caracteres después del '@'")
    
    return (True, "Email válido")

print(validar_email_backend("user@example.com"))
print(validar_email_backend("user@example"))
print(validar_email_backend("@example.com"))
print(validar_email_backend("user@.com"))
