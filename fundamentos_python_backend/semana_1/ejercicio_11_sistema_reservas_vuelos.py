"""Sistema de reservas de vuelos
Contexto: Una aerolínea necesita validar reservas de vuelos según múltiples condiciones.
Reglas de negocio
1. Validaciones básicas
- El pasajero debe tener edad ≥ 18 años (excepto si viaja con adulto)
- El número de pasaporte debe tener entre 6 y 12 caracteres alfanuméricos
- El destino debe ser uno permitido: "MAD", "NYC", "CDMX", "BOG"

2. Clase de vuelo
Clase	                    Equipaje extra incluido	                Precio base
"economy"	                        No	                                $200
"business"	                    1 pieza (23kg)	                        $500
"first"	                       2 piezas (32kg c/u)	                    $1200

3. Reglas adicionales
- Si el pasajero tiene más de 60 años, aplicar 15% descuento
- Si el vuelo es internacional (destino ≠ país de origen = "BOG") y clase "economy" → +$80
- Si el pasajero viaja con mascota → +$50
- Si el destino es "MAD" (Madrid) y clase "first" → upgrade a suite (mostrar mensaje)

4. Límites por clase
- "economy": máximo 2 maletas adicionales pagando $40 c/u
- "business": máximo 3 maletas adicionales pagando $60 c/u
- "first": máximo 4 maletas adicionales pagando $80 c/u

Datos de entrada que solicitar
- Edad del pasajero
- Viaja con adulto acompañante? (s/n)
- Número de pasaporte
- Destino (MAD, NYC, CDMX, BOG)
- Clase (economy, business, first)
- Viaja con mascota? (s/n)
- Cantidad de maletas adicionales """

print("\n=== SISTEMA DE RESERVA DE VUELOS ===\n")

# 1. Edad
entrada_edad = input("Edad del pasajero: ").strip()
try:
    edad = int(entrada_edad)
    if edad <= 0:
        raise ValueError("La edad debe ser mayor que 0.")
except ValueError as e:
    print(f"❌ Error: {e}")
    exit()

# 2. Acompañante
entrada_acompanante = input("¿Viaja con adulto acompañante? (s/n): ").strip().lower()
adulto_acompanante = entrada_acompanante == 's'

if edad < 18 and not adulto_acompanante:
    print("❌ Error: Pasajero menor de edad debe viajar con acompañante.")
    exit()

# 3. Pasaporte
pasaporte = input("Número de pasaporte: ").strip()
if not pasaporte.isalnum():
    print("❌ Error: El pasaporte solo puede contener letras y números.")
    exit()
if len(pasaporte) < 6 or len(pasaporte) > 12:
    print("❌ Error: El pasaporte debe tener entre 6 y 12 caracteres.")
    exit()

# 4. Destino
destinos_permitidos = ["MAD", "NYC", "CDMX", "BOG"]
destino = input("Destino (MAD, NYC, CDMX, BOG): ").strip().upper()
if destino not in destinos_permitidos:
    print("❌ Error: Destino no válido.")
    exit()

# 5. Clase
clases_permitidas = ["economy", "business", "first"]
clase = input("Clase (economy, business, first): ").strip().lower()
if clase not in clases_permitidas:
    print("❌ Error: Clase no válida.")
    exit()

# Configurar según clase
if clase == "economy":
    precio_base = 200
    maletas_max = 2
    costo_maleta_extra = 40
elif clase == "business":
    precio_base = 500
    maletas_max = 3
    costo_maleta_extra = 60
else:  # first
    precio_base = 1200
    maletas_max = 4
    costo_maleta_extra = 80

# 6. Mascota
entrada_mascota = input("¿Viaja con mascota? (s/n): ").strip().lower()
con_mascota = entrada_mascota == 's'
costo_mascota = 50 if con_mascota else 0

# 7. Maletas adicionales
entrada_maletas = input("Cantidad de maletas adicionales: ").strip()
try:
    maletas_extra = int(entrada_maletas)
    if maletas_extra < 0:
        raise ValueError("No puede ser negativo")
    if maletas_extra > maletas_max:
        print(f"Advertencia: Máximo {maletas_max} maletas. Se ajustará a {maletas_max}")
        maletas_extra = maletas_max
except ValueError as e:
    print(f"❌ Error: {e}")
    exit()

costo_maletas = maletas_extra * costo_maleta_extra

# 8. Costo internacional (si aplica)
es_internacional = destino != "BOG"
costo_internacional = 0
if es_internacional and clase == "economy":
    costo_internacional = 80
elif es_internacional and clase == "business":
    costo_internacional = 0
elif es_internacional and clase == "first":
    costo_internacional = 0

# 9. Descuento por edad
descuento_edad = 0
if edad > 60:
    descuento_edad = precio_base * 0.15

# 10. Calcular total
precio_total = precio_base + costo_maletas + costo_mascota + costo_internacional - descuento_edad

# 11. Beneficio especial
beneficio = (destino == "MAD" and clase == "first")

# Mostrar resultados
print("\n--- VALIDACIONES ---")
print(f"Edad válida: {edad} años")
print(f"Pasaporte válido: {len(pasaporte)} caracteres")
print(f"Destino: {destino} ({'Internacional' if es_internacional else 'Nacional'})")
print(f"Clase: {clase}")

print("\n--- DETALLE DE RESERVA ---")
print(f"Pasajero: {edad} años")
print(f"Destino: {destino}")
print(f"Clase: {clase}")
print(f"Mascota: {'Sí (+$50)' if con_mascota else 'No'}")
print(f"Maletas adicionales: {maletas_extra}/{maletas_max}")

print("\n--- COSTOS ---")
print(f"Precio base: ${precio_base}")
if descuento_edad > 0:
    print(f"Descuento por edad (15%): -${descuento_edad:.2f}")
if costo_maletas > 0:
    print(f"Maletas adicionales: {maletas_extra} × ${costo_maleta_extra} = ${costo_maletas}")
if con_mascota:
    print(f"Mascota: +${costo_mascota}")
if costo_internacional > 0:
    print(f"Recargo internacional: +${costo_internacional}")
print(f"\nTotal sin impuestos: ${precio_total:.2f}")

if beneficio:
    print(f"\nBENEFICIO: Upgrade a suite por volar first a Madrid")