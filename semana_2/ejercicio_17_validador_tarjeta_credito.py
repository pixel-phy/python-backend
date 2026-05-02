"""Validador de tarjeta de crédito:
Validar datos de entrada de usuarios (tarjetas, formularios, etc..)

1. Pedir número de tarjeta (como string, porque puede tener espacios)
2. Eliminar espacios con .replace()
3. Validar:
- Tenga exactamente 16 dígitos
- Todos sean dígitos
- Primer dígito: 4: Visa, 51 a 55 : Mastercard, 34 0 37: American Express
4. Mostrar el tipo o desconocido. """

print("\n=== VALIDADOR DE TARJETAS DE CRÉDITO ===\n")

while True:
    entrada = input("Número (XXXX XXXX XXXX XXXX): ").strip()
    numero = entrada.replace(" ", "")
    
    if len(numero) != 16:
        print("El número debe tener exactamente 16 dígitos.\n")
        continue
    
    if not numero.isdigit():
        print("El número solo puede contener dígitos.\n")
        continue
    
    # Verificar tipo de tarjeta
    primeros_dos = numero[0:2]  # primeros 2 dígitos
    primer_digito = numero[0]
    
    if primer_digito == '4':
        tipo = "Visa"
        print("✅ Tarjeta válida")
    elif primer_digito == '5' and primeros_dos >= '51' and primeros_dos <= '55':
        tipo = "MasterCard"
        print("✅ Tarjeta válida")
    elif primeros_dos == '34' or primeros_dos == '37':
        tipo = "American Express"
        print("✅ Tarjeta válida")
    else:
        tipo = "Desconocido"
        print("Tarjeta válida pero tipo no reconocido")
    
    print(f"Tipo: {tipo}")
    break