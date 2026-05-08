"""Escribe un programa que:
1. Pida un string al usuario.
2. Verifique si:
- Solo tiene letras.
- Solo tiene números.
- Solo tiene letras y números.
- Está en mayúsculas.
- Está en minúsculas. """

texto = input("Ingrese una cadena de texto: ").strip()

print("\n--- Resultados ---\n")
print(f"Texto: '{texto}'\n")

if texto.isalpha():
    print("✅ Solo letras")
else:
    print("❌ No solo letras")

if texto.isdigit():
    print("✅ Solo números")
else:
    print("❌ No solo números")

if texto.isalnum():
    print("✅ Solo letras y números (sin espacios)")
else:
    print("❌ Contiene otros caracteres (espacios, símbolos)")

if texto.isupper():
    print("✅ Todo mayúsculas")
else:
    print("❌ No todo mayúsculas")

if texto.islower():
    print("✅ Todo minúsculas")
else:
    print("❌ No todo minúsculas")

if " " in texto:
    print("✅ Tiene espacios")
else:
    print("❌ No tiene espacios")