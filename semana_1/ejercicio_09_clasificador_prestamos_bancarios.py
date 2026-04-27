""" Clasificador de préstamos bancarios
Contexto: Un banco clasifica solicitudes de préstamo según múltiples reglas.

Reglas completas
Condición	                                            Resultado
Edad < 18	                                    ❌ Rechazo automático
Edad > 70 y monto ≥ $5000	                        ❌ Rechazo
Historial crediticio = "malo"	                ❌ Rechazo automático
Historial = "regular" y monto > $5000	            ❌ Rechazo
Monto < $1000	                                ✅ Préstamo rápido
Monto entre $1000 y $10000 (inclusive)	        ✅ Requiere análisis
Monto > $10000	                                ✅ Requiere garantía

Requisitos del programa:
Solicitar:
1. Edad.
2. Historial crediticio (bueno, regular, malo).
3. Monto solicitado.
Validar:
4. Edad entre 0 y 120.
5. Historial sea uno de los 3 valores.
6. Monto > 0.
Mostrar:
7. Si es aprobado o rechazado.
8. El motivo del rechazo (si aplica).
9. El tipo de préstamo (si aplica)."""

print("\n=== CLASIFICADOR DE PRESTAMOS BANCARIOS ===\n")

# 1. Edad
entrada_edad = input("Edad: ").strip()
try:
    edad = int(entrada_edad)
    if edad <= 0 or edad > 120:
        raise ValueError("La edad debe estar entre 1 y 120 años.")
except ValueError as e:
    print(f"❌ Error: {e}")
    exit()

if edad < 18:
    print("❌ Rechazo: Edad mínima 18 años")
    exit()

# 2. Historial
historiales_validos = ["bueno", "regular", "malo"]
entrada_historial = input("Historial (bueno/regular/malo): ").strip().lower()

if entrada_historial not in historiales_validos:
    print("❌ Error: El historial debe ser bueno, regular o malo")
    exit()

if entrada_historial == "malo":
    print("❌ Rechazo: Historial crediticio malo")
    exit()

# 3. Monto
entrada_monto = input("Monto solicitado: ").strip()
try:
    monto_solicitado = float(entrada_monto)
    if monto_solicitado <= 0:
        raise ValueError("El monto debe ser mayor a 0")
except ValueError as e:
    print(f"❌ Error: {e}")
    exit()

# 4. Reglas de negocio
if edad > 70 and monto_solicitado >= 5000:
    print("❌ Rechazo: Edad > 70 y monto ≥ $5000")
elif entrada_historial == "regular" and monto_solicitado > 5000:
    print("❌ Rechazo: Historial regular + monto > $5000")
else:
    print("✅ Aprobado")
    
    if monto_solicitado < 1000:
        print("   Tipo: Préstamo rápido (< $1000)")
    elif monto_solicitado <= 10000:
        print("   Tipo: Requiere análisis ($1000 - $10000)")
    else:
        print("   Tipo: Requiere garantía (> $10000)")