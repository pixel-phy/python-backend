"""Validador de placa de carro:
Un sistema de peajes necesita validar que las placas tengan el formato correcto.
Reglas: 
- 3 letras + 3 números 
- No puede tener espacios
- Todas las letras  mayúsculas 
Escriba un programa que:
1. Pida la placa.
2. Valide el formato (3 letras + 3 números)
3. Muestre placa válida "✅ Placa válida" o "❌ Placa inválida" con el motivo """

print("\n=== VALIDADOR DE PLACAS ===\n")

print("\n=== VALIDADOR DE PLACAS ===\n")

while True:
    placa = input("Placa: ").strip()

    # Validaciones
    if len(placa) != 6:
        print("❌ Debe tener exactamente 6 caracteres (3 letras + 3 números)")
        continue

    if " " in placa:
        print("❌ No debe contener espacios")
        continue

    primeras = placa[:3]
    ultimas = placa[3:]

    if not primeras.isalpha():
        print("❌ Los primeros 3 caracteres deben ser letras")
        continue

    if not primeras.isupper():
        print("❌ Las letras deben estar en mayúsculas")
        continue

    if not ultimas.isdigit():
        print("❌ Los últimos 3 caracteres deben ser números")
        continue

    # Si pasa todas
    print(f"✅ Placa válida: {placa}")
    break