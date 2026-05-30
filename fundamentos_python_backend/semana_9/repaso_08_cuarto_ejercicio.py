""" Eliminar elementos en un diccionario:
Dada la sesión de usuario. 
1. Elimina "cache_temp" (no necesitas su valor)
2. Eliminar "token" pero guardar su valor en una variable token_eliminado.
3. Eliminar el último elemento y guardar el resultado en ultimo
4. Imprime:
    - El valor de token_eliminado
    - El valor de ultimo
    - El diccionario sesion final """

sesion = {
        "usuario_id": 456,
        "nombre": "Laura",
        "token": "abc123xyz",
        "ultimo_movimiento": "2026-05-30",
        "cache_temp": "datos temporales"
    }

del sesion["cache_temp"]
token_eliminado = sesion.pop("token")
ultimo = sesion.popitem()
print(f"token eliminado: {token_eliminado}")
print(f"ultimo: {ultimo}")
print(sesion)
