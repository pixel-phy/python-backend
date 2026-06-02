"""Validador de email
Típico en APIs de registro """

def validar_email(email):
    """Verifica si el email tiene formato básico válido"""
    if "@" not in email:
        return False
    if "." not in email.split("@")[-1]:
         return False
    return True

# Uso en un endpoint de registro
email_usuario = "carlos@backend.com"
if validar_email(email_usuario):
    print("Email válido, continuar con registro")
else:
    print("Email inválido, rechazar solicitud")

