""" Docstrings y buenas pŕacticas
En el Backend en código casi nunca lo escribe una sola persona. Trabajando en equipo, o incluso para uno mismo en el futuro, es 
vital que las funciones estén documentadas. Para eso usamos docstrings. Un Docstring es un texto especial que se coloca justo debajo 
de la definición de la función (usando triple comilla) para explicar qué hace, qué recibe y qué devuelve.

def validar_y_crear_usuario(username: str, email: str, password: str) -> tuple:
    '''
    Valida los datos de un formulario de registro y crea un usuario.

    Args:
        username (str): El nombre de usuario (mínimo 4 caracteres).
        email (str): El correo electrónico (debe contener '@').
        password (str): La contraseña de seguridad (mínimo 6 caracteres).

    Returns:
        tuple: Un par (bool, str/dict) donde el primer elemento indica el éxito 
               y el segundo contiene el mensaje de error o los datos del usuario.
    '''
     # Código de la función


