"""EXTRAER DOMINIO DE UN CORREO ELECTRÓNICO
Una empresa necesita extraer el dominio de los correos de sus clientes (para estadísticas, filtros, etc.)
Escribir un programa que:
1. Solicite un correo electrónico al usuario.
2. Extraiga el dominio (Todo lo que está después del @)
3. Valide que el correo tenga un formato mínimo:
- Contiene un @
- El @ no está al inicio ni al final
- Después del @ hay al menos un .
4. Muestre el dominio en minúsculas."""

print("\n === VALIDADOR DE DOMINIO EN CORREOS ===\n")
while True:
    correo = input("Correo electrónico: ").strip()

    if not "@" in correo:
        print("El correo debe contener un '@'\n")
        continue

    if correo[0] == '@' or correo[-1] == '@':
        print("El @ no debe estar al inicio ni al final del correo.\n")
        continue

    posicion = correo.find("@")
    if not "." in correo[posicion:]:
        print("El correo debe tener al menos un punto (.) después del @.\n")
        continue

    dominio = correo[posicion + 1:]
    print(f"\nEl dominio del correo es: {dominio.lower()}") # Por si escribe el dominio en mayúsculas.
    break