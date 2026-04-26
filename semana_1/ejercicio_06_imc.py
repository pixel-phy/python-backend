"""Estás desarrollando una aplicación de salud y bienestar que calcula el Índice de Masa Corporal (IMC)
 de una persona y le da recomendaciones personalizadas según su resultado y edad.
 
 IMC = peso / (altura ** 2)
 
 IMC	            Clasificación	            Recomendación
< 18.5	            Bajo peso	         "Consulta a un nutricionista"
18.5 - 24.9	        Normal	             "Mantén tus hábitos saludables"
25 - 29.9	        Sobrepeso	          "Considera hacer ejercicio regularmente"
≥ 30	            Obesidad	         "Riesgo alto, consulta a un médico"

Reglas adicionales
1. Si la persona tiene sobrepeso Y es mayor de 50 años → mostrar "⚠️ ALTO RIESGO: combina sobrepeso con edad avanzada"
2. Si la persona tiene obesidad Y es mayor de 40 años → mostrar "⚠️ CRÍTICO: obesidad + edad > 40, requiere atención inmediata"
3. Si el IMC es Normal pero la persona tiene menos de 18 años → mostrar "📌 Seguimiento pediátrico recomendado"

Requisitos del programa
Solicitar al usuario:
1. Peso (kg)
2. Altura (metros)
3. Edad (años)

Validar:
1. Peso > 0 y < 500
2. Altura > 0 y < 3
3. Edad > 0 y < 120

Calcular el IMC con 2 decimales
Mostrar:
1. IMC calculado
2. Clasificación
3. Recomendación base

Advertencias adicionales (si aplica):
1. Si la persona tiene sobrepeso Y es mayor de 50 años → mostrar:  "ALTO RIESGO: combina sobrepeso con edad avanzada"
2. Si la persona tiene obesidad Y es mayor de 40 años → mostrar:   "CRÍTICO: obesidad + edad > 40, requiere atención inmediata"
3. Si el IMC es Normal pero la persona tiene menos de 18 años → mostrar: "Seguimiento pediátrico recomendado"""

print("\n=== ÍNDICE DE MASA CORPORAL APLICACIÓN ===\n")

# Datos de usuario
entrada_peso = input("Ingrese peso (kg): ").strip()
try:
    peso = float(entrada_peso)
    if peso <= 0 or peso > 500:
        raise ValueError("El valor del peso debe estar entre 0 y 500 kg.")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
    exit()

entrada_altura = input("Ingrese estatura (m): ").strip()
try:
    altura = float(entrada_altura)
    if altura <= 0 or altura > 3:
        raise ValueError("El valor de la estatura debe estar entre 0 y 3 metros.")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
    exit()

try:
    edad = int(input("Ingrese edad: "))
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120 años.")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
    exit()

# Calculamos IMC
imc = peso / (altura ** 2)

# Clasificación según IMC
if imc < 18.5:
    estado = "bajo peso"
    recomendacion = "Consulta con un nutricionista"
elif imc < 25:  # 18.5 a 24.9
    estado = "normal"
    recomendacion = "Mantén tus hábitos saludables"
elif imc < 30:  # 25 a 29.9
    estado = "sobrepeso"
    recomendacion = "Considera hacer ejercicio regularmente"
else: 
    estado = "obesidad"
    recomendacion = "Riesgo alto. Consulta a un médico"

# Advertencias adicionales (inicializamos como cadena vacía)
advertencia = ""

if estado == "sobrepeso" and edad > 50:
    advertencia = "ALTO RIESGO: combina sobrepeso con edad avanzada"
elif estado == "obesidad" and edad > 40:
    advertencia = f"CRÍTICO: obesidad + edad {edad} > 40, requiere atención inmediata"
elif estado == "normal" and edad < 18:
    advertencia = "Seguimiento pediátrico recomendado"

# Mostramos resultados
print("\n--- RESULTADOS ---\n")
print(f"Peso: {peso:.1f} kg")
print(f"Altura: {altura:.2f} m")
print(f"Edad: {edad} años")
print()
print(f"IMC: {imc:.2f} ({estado})")
print(f"Recomendación: {recomendacion}")

if advertencia:  # Solo mostrar si no está vacía
    print(advertencia)