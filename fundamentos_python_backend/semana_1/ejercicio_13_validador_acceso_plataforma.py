"""Validador de acceso a plataforma de streaming
Contexto:
Una plataforma de streaming necesita validar si un usuario puede acceder a cierto contenido según su plan, edad y dispositivo.

Reglas de negocio
Plan	                            Acceso a contenido +18	            Límite de dispositivos	                Precio mensual
"básico"	                                ❌ No	                        1 dispositivo	                        $5.99
"estándar"	                                ❌ No	                        2 dispositivos	                        $9.99
"premium"	                                ✅ Sí	                        4 dispositivos	                        $14.99
Reglas adicionales
Edad: Para ver contenido +18, el usuario debe tener edad ≥ 18 años
Descuentos:
Si el usuario tiene edad ≥ 65 años: 30% de descuento
Si el usuario paga anualmente (12 meses): 20% de descuento adicional sobre el precio con descuento
Límite de dispositivos: No puede exceder el límite del plan

Validaciones:
Plan debe ser válido (básico, estándar, premium)
Edad entre 0 y 120 años
Dispositivos conectados debe ser ≥ 1
Datos que debe solicitar el programa
Plan del usuario (básico, estándar, premium)
Edad del usuario
Dispositivos conectados actualmente (número)
Tipo de pago (mensual o anual)

"""

print("\n=== VALIDADOR DE PLATAFORMA STREAMING ===\n")

# 1. ENTRADAS
planes_usuario = ["básico", "estándar", "premium"]
entrada_plan = input("Plan (básico/estándar/premium): ").strip().lower()

if entrada_plan not in planes_usuario:
    print("❌ Plan no válido")
    exit()

entrada_edad = input("Edad: ").strip()
try:
    edad = int(entrada_edad)
    if edad <= 0 or edad > 120:
        raise ValueError("Edad entre 1 y 120")
except ValueError as e:
    print(f"❌ Error: {e}")
    exit()

entrada_dispositivos = input("Dispositivos conectados: ").strip()
try:
    dispositivos = int(entrada_dispositivos)
    if dispositivos < 1:
        raise ValueError("Mínimo 1 dispositivo")
except ValueError as e:
    print(f"❌ Error: {e}")
    exit()

opciones_pago = ["mensual", "anual"]
entrada_pago = input("Tipo de pago (mensual/anual): ").strip().lower()
if entrada_pago not in opciones_pago:
    print("❌ Tipo de pago no válido")
    exit()

# 2. VARIABLES PARA RESULTADOS (inicializar)
contenido_adultos = False
dispositivos_max = 1
precio_base = 0.0
precio_final = 0.0
descuento_edad_aplicado = 0
descuento_anual_aplicado = 0
acceso_denegado_razon = ""

# 3. CONFIGURACIÓN SEGÚN PLAN
if entrada_plan == "básico":
    contenido_adultos = False
    dispositivos_max = 1
    precio_base = 5.99
elif entrada_plan == "estándar":
    contenido_adultos = False
    dispositivos_max = 2
    precio_base = 9.99
else:  # premium
    contenido_adultos = True
    dispositivos_max = 4
    precio_base = 14.99

# 4. VERIFICAR LÍMITE DE DISPOSITIVOS
if dispositivos > dispositivos_max:
    acceso_denegado_razon = f"Demasiados dispositivos: {dispositivos}/{dispositivos_max}"
    precio_final = 0  # No se calcula precio si no hay acceso

# 5. CALCULAR PRECIO (solo si hay acceso a dispositivos)
if not acceso_denegado_razon:
    precio_final = precio_base
    
    # Descuento por edad (≥ 65)
    if edad >= 65:
        descuento_edad_aplicado = 30
        precio_final = precio_final * (1 - 0.30)
    
    # Descuento por pago anual
    if entrada_pago == "anual":
        descuento_anual_aplicado = 20
        precio_final = precio_final * (1 - 0.20)

# 6. ACCESO A CONTENIDO +18
acceso_18 = contenido_adultos and edad >= 18

# 7. MOSTRAR RESULTADOS
print("\n--- VALIDACIONES ---")
print(f"✅ Plan: {entrada_plan}")
print(f"✅ Edad: {edad} años")
if acceso_denegado_razon:
    print(f"❌ Dispositivos: {dispositivos}/{dispositivos_max} - {acceso_denegado_razon}")
else:
    print(f"✅ Dispositivos: {dispositivos}/{dispositivos_max}")

print("\n--- CONTENIDO +18 ---")
if acceso_18:
    print("✅ Acceso permitido a contenido +18")
else:
    if not contenido_adultos:
        print(f"❌ Acceso denegado: plan {entrada_plan} no incluye +18")
    elif edad < 18:
        print(f"❌ Acceso denegado: edad {edad} < 18")

print("\n--- CÁLCULOS ---")
if acceso_denegado_razon:
    print("⚠️ No se calculó precio por exceso de dispositivos")
else:
    print(f"Precio base: ${precio_base:.2f}")
    if descuento_edad_aplicado > 0:
        print(f"Descuento por edad (≥65): {descuento_edad_aplicado}%")
    else:
        print("Descuento por edad: No aplica")
    
    if descuento_anual_aplicado > 0:
        print(f"Descuento por pago anual: {descuento_anual_aplicado}%")
    else:
        print("Descuento por pago anual: No aplica")
    
    print(f"Precio final: ${precio_final:.2f}/mes")

print("\n--- RESUMEN ---")
if acceso_denegado_razon:
    print(f"❌ ACCESO DENEGADO: {acceso_denegado_razon}")
else:
    print(f"✅ Plan: {entrada_plan}")
    print(f"💰 Precio final: ${precio_final:.2f}/mes")