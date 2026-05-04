"""Extractor de iniciales en nombres:
Un sistema necesita generar las iniciales de un nombre completo.
- Tomar la primera letra de cada palabra.
- Ponerla en mayúscula.
- Separar con punto (.)
- Agregar punto al final."""

print("\n=== EXTRACTOR DE INICIALES ===\n")
while True:
    nombre = input("Nombre completo: ").strip()
    
    # Valido que solo tenga letras y espacios
    valido = True
    for letra in nombre:
        if not (letra.isalpha() or letra == " "):
            valido = False
            break
    
    if not valido:
        print("El nombre solo puede contener letras y espacios.\n")
        continue

    #Extraer iniciales
    iniciales = nombre[0].upper() + "."
    for letra in range(len(nombre)):
        if nombre[letra] == " " and letra + 1 < len(nombre):
            iniciales += nombre[letra + 1].upper() + "."
    
    print(f"Iniciales: {iniciales}")
    break