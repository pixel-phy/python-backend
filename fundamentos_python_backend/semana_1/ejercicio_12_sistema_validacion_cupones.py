"""Reglas de cupones (simplificadas)
Una tienda online quiere implementar un sistema de validación de cupones promocionales. 
Los clientes ingresan un código y el sistema debe verificar si es válido según las reglas de negocio, 
aplicar el descuento correspondiente y mostrar el total a pagar.
Cupones disponibles
La tienda ofrece 5 cupones con diferentes reglas:
Código	                            Descuento	                    Reglas especiales
"AHORRO10"	                    10%	de descuento                        Compra mínima $50
"AHORRO20"	                    20%	de descuento                        Compra mínima $100
"ENVIOGRATIS"	                        $0 envío	                Compra mínima $30
"SUPEROFERTA"	                15% de descuento	                Solo si es fin de semana (sábado o domingo)
"BIENVENIDA"	                10%	de descuento                Primera compra (marcar con variable booleana)
Reglas generales que aplican para TODOS los cupones
1. El código del cupón debe ser exactamente uno de los 5 (no distingue mayúsculas/minúsculas)
2. El monto de compra debe ser mayor a $0
3. El costo de envío no puede ser negativo
4. Si el cupón no cumple su requisito específico, se debe rechazar con un mensaje claro

Datos que solicitar
1. Código del cupón
2. Monto de compra
3. Costo de envío
4. ¿Es primera compra? (s/n)
5. Día de la semana (lunes a domingo)"""
print("\n=== VALIDADOR DE CUPONES DE DESCUENTO ===\n")

# 1. ENTRADAS
cupones_validos = ["AHORRO10", "AHORRO20", "ENVIOGRATIS", "SUPEROFERTA", "BIENVENIDA"]
entrada_cupon = input("Código del cupón: ").strip().upper()

if entrada_cupon not in cupones_validos:
    print("Cupón no válido")
    exit()
else:
    print(f"Cupón válido: {entrada_cupon}")

# Monto de compra
entrada_monto = input("Monto de compra: ").strip()
try:
    monto_compra = float(entrada_monto)
    if monto_compra <= 0:
        raise ValueError("El monto debe ser mayor a 0")
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Costo de envío
entrada_envio = input("Costo de envío: ").strip()
try:
    costo_envio = float(entrada_envio)
    if costo_envio < 0:
        raise ValueError("El costo de envío no puede ser negativo")
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Primera compra
entrada_primera_compra = input("¿Es primera compra? (s/n): ").strip().lower()
primera_compra = entrada_primera_compra == 's'

# Día de la semana
dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
entrada_dia = input("Día de la semana (lunes a domingo): ").strip().lower()
if entrada_dia not in dias_semana:
    print("Día no válido")
    exit()

# 2. VARIABLES PARA RESULTADOS (inicializamos)
cupon_aplicado = False
porcentaje_descuento = 0
descuento = 0
costo_envio_final = costo_envio
total = 0
razon_rechazo = ""

# 3. REGLAS POR CUPÓN
if entrada_cupon == "AHORRO10" and monto_compra >= 50:
    cupon_aplicado = True
    porcentaje_descuento = 10
    descuento = monto_compra * porcentaje_descuento / 100
    total = monto_compra + costo_envio - descuento

elif entrada_cupon == "AHORRO20" and monto_compra >= 100:
    cupon_aplicado = True
    porcentaje_descuento = 20
    descuento = monto_compra * porcentaje_descuento / 100
    total = monto_compra + costo_envio - descuento

elif entrada_cupon == "ENVIOGRATIS" and monto_compra >= 30:
    cupon_aplicado = True
    costo_envio_final = 0
    total = monto_compra + costo_envio_final

elif entrada_cupon == "SUPEROFERTA" and (entrada_dia == "sabado" or entrada_dia == "domingo"):
    cupon_aplicado = True
    porcentaje_descuento = 15
    descuento = monto_compra * porcentaje_descuento / 100
    total = monto_compra + costo_envio - descuento

elif entrada_cupon == "BIENVENIDA" and primera_compra:
    cupon_aplicado = True
    porcentaje_descuento = 10
    descuento = monto_compra * porcentaje_descuento / 100
    total = monto_compra + costo_envio - descuento

else:
    # El cupón existe pero no cumple requisitos
    cupon_aplicado = False
    if entrada_cupon == "AHORRO10":
        razon_rechazo = f"Monto mínimo $50 (ingresaste ${monto_compra})"
    elif entrada_cupon == "AHORRO20":
        razon_rechazo = f"Monto mínimo $100 (ingresaste ${monto_compra})"
    elif entrada_cupon == "ENVIOGRATIS":
        razon_rechazo = f"Monto mínimo $30 (ingresaste ${monto_compra})"
    elif entrada_cupon == "SUPEROFERTA":
        razon_rechazo = f"Solo válido fines de semana (ingresaste {entrada_dia})"
    elif entrada_cupon == "BIENVENIDA":
        razon_rechazo = "Solo válido en primera compra"

# 4. MOSTRAR RESULTADOS
print("\n--- VALIDACIONES ---")
if entrada_cupon in cupones_validos:
    print(f"Cupón válido: {entrada_cupon}")

print("\n--- CUPÓN APLICADO ---")
if cupon_aplicado:
    print("Cupón aplicado exitosamente")
else:
    print(f"Cupón rechazado: {razon_rechazo}")

if cupon_aplicado:
    print("\n--- CÁLCULOS ---")
    print(f"Monto original: ${monto_compra:.2f}")
    
    if entrada_cupon != "ENVIOGRATIS":
        print(f"Descuento: {porcentaje_descuento}% = ${descuento:.2f}")
        print(f"Costo de envío: ${costo_envio:.2f}")
        print(f"Total a pagar: ${total:.2f}")
    else:
        print(f"Costo de envío original: ${costo_envio:.2f}")
        print(f"Costo de envío con cupón: ${costo_envio_final:.2f}")
        print(f"Total a pagar: ${total:.2f}")