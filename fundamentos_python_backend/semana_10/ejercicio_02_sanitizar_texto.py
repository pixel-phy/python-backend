"""Sanitizar entrada de usuario
Evitar inyección básica """

def sanitizar_texto(texto):
    """Elimina caracteres peligrosos para consultas"""
    caracteres_peligrosos = ["'", '"', ";", "--"]
    for char in caracteres_peligrosos:
        texto = texto.replace(char, "")
    return texto.strip()

# Uso antes de procesar datos
input_usuario = "Robert'; DROP TABLE users;--"
limpio = sanitizar_texto(input_usuario)
print(f"Original: {input_usuario}")
print(f"Sanitizado: {limpio}")
