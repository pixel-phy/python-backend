""" Conteo de frecuencias (aplicación real en Backend)
Un sistema necesita contar cuántas veces aparece cada palabra en un texto, o cuántos estudiantes hay por curso, etc. Los diccionarios son ideales para esto. """

# Ejemplo 1: Contar letras en una palabra
palabra = "programacion"
frecuencias = {}

for letra in palabra:
    if letra in frecuencias:
        frecuencias[letra] += 1
    else:
        frecuencias[letra] = 1

print("--- FRECUENCIA DE LETRAS ---")
for letra, cantidad in frecuencias.items():
    print(f"'{letra}': {cantidad} vez/veces")

# Ejemplo 2: Contar palabras en una frase
frase = "el perro corre y el gato duerme y el pajaro vuela"
palabras = frase.split()
conteo = {}

for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print("\n--- FRECUENCIA DE PALABRAS ---")
for palabra, cantidad in conteo.items():
    print(f"'{palabra}': {cantidad} vez/veces")

# Ejemplo 3: Contar estudiantes por curso
estudiantes = [
        ("Ana", "Matemáticas"),
        ("Luis", "Ciencias"),
        ("Carlos", "Matemáticas"),
        ("Sofia", "Ciencias"),
        ("Juan", "Arte"),
        ("Maria", "Matemáticas")
        ]

curso_conteo = {}
for nombre, curso in estudiantes:
    if curso in curso_conteo:
        curso_conteo[curso] += 1
    else:
        curso_conteo[curso] = 1

print("\n--- ESTUDIANTES POR CURSO ---")
for curso, cantidad in curso_conteo.items():
    print(f"{curso}: {cantidad} estudiante(s)")

# Contar vocales en la palabra 'esternocleidomastoideo'
palabra = "esternocleidomastoideo"
frecuencias = {}

for letra in palabra:
    if letra in "aeiou":
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1

print("\n--- FRECUENCIAS DE VOLCALES ---")
for vocal, cantidad in frecuencias.items():
    print(f"'{vocal}': {cantidad} vez/veces")

# 2. Contar palabras en la frase:
frase = "la casa es bonita y la casa es grande y la casa es amarilla"
palabras = frase.split()
conteo = {}

for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

max_cantidad = 0
palabra_repetida = ""

for palabra, cantidad in conteo.items():
    if cantidad > max_cantidad:
        max_cantidad = cantidad
        palabra_repetida = palabra

print("\n--- FRECUENCIA DE PALABRAS ---")
for palabra, cantidad in conteo.items():
    print(f"'{palabra}': {cantidad} vez/veces")

print(f"\n La palabra más repetida es '{palabra_repetida}' con {max_cantidad} veces")

# 3. Dada la lista contar cuántas veces aparece cada número usando un diccionario
numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
conteo = {}
for numero in numeros:
    if str(numero) in conteo:
        conteo[str(numero)] += 1
    else:
        conteo[str(numero)] = 1

print("\n--- FRECUENCIA DE NÚMEROS ---")
for numero, cantidad in conteo.items():
    print(f"'{numero}': {cantidad} veces")
