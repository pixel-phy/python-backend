""" Sistema de envíos por zona
Contexto: Una empresa de logística calcula costo de envío según la zona y el peso del paquete.
Reglas:
Zona	                            Costo base	                            Factor por kg extra
1 (Local)	                            $5	                                +$0.50 por kg > 5kg
2 (Regional)	                        $10	                                +$1 por kg > 3kg
3 (Nacional)	                        $20	                                +$2 por kg > 2kg
4 (Internacional)	                    $50                             	+$5 por kg > 1kg
Además:
1. Si peso > 20kg → ❌ "No se puede enviar"
2. Si zona 4 y peso > 10kg → +$30 (gastos de aduana)

Fórmula general:
Costo total = Costo base + (kg extra × factor) + costo aduana (si aplica)

Nota: "kg extra" es el peso que supera el límite gratuito de cada zona."""
print("\n=== SISTEMA DE ENVÍOS POR ZONA ===\n")

# Zona
entrada_zona = input("Ingrese el número de zona (1 Local, 2 Regional, 3 Nacional, 4 Internacional): ").strip()
try:
    zona = int(entrada_zona)
    if zona < 1 or zona > 4:
        raise ValueError("La zona debe ser 1, 2, 3 o 4")
except ValueError as e:
    print(f"❌ Error: {e}")
    exit()

# Peso
entrada_peso = input("Peso del paquete (kg): ").strip()
try:
    peso = float(entrada_peso)
    if peso <= 0:
        raise ValueError("El peso debe ser mayor a 0 kg")
except ValueError as e:
    print(f"❌ Error: {e}")
    exit()

# Validar peso máximo
if peso > 20:
    print("❌ No se puede enviar: Peso máximo 20 kg")
    exit()

print("\n--- Resultado ---\n")

# Zona 1: Local
if zona == 1:
    nombre_zona = "Local"
    costo_base = 5
    limite_gratis = 5
    costo_extra = 0
    
    if peso > limite_gratis:
        extra = peso - limite_gratis
        costo_extra = extra * 0.5
        print(f"Zona: {nombre_zona}")
        print(f"Peso: {peso} kg")
        print(f"Costo base: ${costo_base}")
        print(f"Peso extra: {extra} kg x $0.50 = ${costo_extra}")
    else:
        print(f"Zona: {nombre_zona}")
        print(f"Peso: {peso} kg")
        print(f"Costo base: ${costo_base}")
        print(f"Peso extra: No aplica")
    
    costo_total = costo_base + costo_extra
    print(f"Costo total: ${costo_total:.2f}")

# Zona 2: Regional
elif zona == 2:
    nombre_zona = "Regional"
    costo_base = 10
    limite_gratis = 3
    costo_extra = 0
    
    if peso > limite_gratis:
        extra = peso - limite_gratis
        costo_extra = extra * 1
        print(f"Zona: {nombre_zona}")
        print(f"Peso: {peso} kg")
        print(f"Costo base: ${costo_base}")
        print(f"Peso extra: {extra} kg x $1 = ${costo_extra}")
    else:
        print(f"Zona: {nombre_zona}")
        print(f"Peso: {peso} kg")
        print(f"Costo base: ${costo_base}")
        print(f"Peso extra: No aplica")
    
    costo_total = costo_base + costo_extra
    print(f"Costo total: ${costo_total:.2f}")

# Zona 3: Nacional
elif zona == 3:
    nombre_zona = "Nacional"
    costo_base = 20
    limite_gratis = 2
    costo_extra = 0
    
    if peso > limite_gratis:
        extra = peso - limite_gratis
        costo_extra = extra * 2
        print(f"Zona: {nombre_zona}")
        print(f"Peso: {peso} kg")
        print(f"Costo base: ${costo_base}")
        print(f"Peso extra: {extra} kg x $2 = ${costo_extra}")
    else:
        print(f"Zona: {nombre_zona}")
        print(f"Peso: {peso} kg")
        print(f"Costo base: ${costo_base}")
        print(f"Peso extra: No aplica")
    
    costo_total = costo_base + costo_extra
    print(f"Costo total: ${costo_total:.2f}")

# Zona 4: Internacional
elif zona == 4:
    nombre_zona = "Internacional"
    costo_base = 50
    limite_gratis = 1
    costo_extra = 0
    costo_aduana = 0
    
    if peso > limite_gratis:
        extra = peso - limite_gratis
        costo_extra = extra * 5
        print(f"Zona: {nombre_zona}")
        print(f"Peso: {peso} kg")
        print(f"Costo base: ${costo_base}")
        print(f"Peso extra: {extra} kg x $5 = ${costo_extra}")
        
        if peso > 10:
            costo_aduana = 30
            print(f"Gastos de aduana: +${costo_aduana} (por >10 kg)")
    else:
        print(f"Zona: {nombre_zona}")
        print(f"Peso: {peso} kg")
        print(f"Costo base: ${costo_base}")
        print(f"Peso extra: No aplica")
    
    costo_total = costo_base + costo_extra + costo_aduana
    print(f"Costo total: ${costo_total:.2f}")
