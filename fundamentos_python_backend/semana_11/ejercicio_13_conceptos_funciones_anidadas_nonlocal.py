"""Funciones anidadas y la palabra clave nonlocal

Inner functions (funciones anidadas): en el desarrollo de software se usa por dos razones principales:
    Encapsulamiento: Ocultar funciones ayudants para que nadie más pueda usarlas fuera de la función 
    principal (protección de código).
    Fábricas de funciones (Closures): Funciones externas que configuran y devuelven funcinoes internas 
    personalizadas.

El concepto de Ámbito (Scope) e introducción a nonlocal:   
    Cuando anidamos funciones, aparece un nivel intermedio: el ámbito enmarcador o contenedor (enclosing scope).
    Si la función interna quiere modificar una variable de la función externa, Python no la dejará a menos 
    que uses la palabra clave nonlocal. """

# Por ejemplo:
def crear_contador_intentos():
    intentos = 0

    def registrar_intento():
        nonlocal intentos
        intentos += 1
        return f"Intentos de inicio de sesión: {intentos}"
    return registrar_intento

contador_seguridad = crear_contador_intentos()

print(contador_seguridad())
print(contador_seguridad())

"""La variable intentos está completamente protegida. Nadie desde fuera del código puede alterarla o hackearla
directamente, solo se puede modificar ejecutando contador_seguridad()."""




