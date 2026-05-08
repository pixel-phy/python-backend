"""Los métodos básicos son:
upper(), lower (), strip().
Dada la variable: texto = "hola MUNDO" :
1. Mostrar el texto en mayúscula.
2. Mostrar el texto en minúscula.
3. Mostrar el texto con la primera letra en mayúscula y el resto en minúscula.
4. Mostrar el texto sin espacios al inicio ni al final.
5. Mostrar el texto original sin modificar (para ver que los métodos no cambian el valor de la variable original)."""

texto = " hola MUNDO "
texto_mayuscula = texto.upper()
texto_minuscula = texto.lower()
primera_mayuscula = texto.capitalize()
sin_espacios = texto.strip()

print("\n --- RESULTADOS --- \n")
print(f"En mayúsculas: {texto_mayuscula}")
print(f"En munúsculas: {texto_minuscula}")
print(f"Primera mayúscula: {primera_mayuscula}")
print(f"Sin espacios: {sin_espacios}")
print(f"Valor variable: {texto}")