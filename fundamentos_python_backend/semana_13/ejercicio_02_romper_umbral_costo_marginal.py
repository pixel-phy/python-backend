""" Romper el umbral de costo marginal:
    En un model de inventario estocástico, se simulan diferentes escenarios de penalización por 
    desabastecimiento. Tienes una lista de escenarios (cada uno con un ID y el costo asociado).

    • Encuentra el primer escenario donde el costo de penalización sea estrictamente mayor
    que el presupuesto de contingencia de la empresa, pero que además pertenezca a una zona
    logística específica.
    • Restricción: El input de datos puede venir sucio o incompleto. Asegúrate de validar los datos
    de entrada en Python. """

def buscar_escenario(escenarios, presupuesto, zona):

    zona = zona.strip().upper()

    for escenario in escenarios:
        if not escenario or len(escenario) < 3:
            continue

        id_esc, costo_raw, zona_esc = escenario

        try:
            costo = float(costo_raw)
        except (TypeError, ValueError):
            continue

        if not id_esc or not zona_esc:
            continue

        if costo > presupuesto and zona_esc.upper() == zona:
            return (str(id_esc), costo, str(zona_esc))

    return None

# Prueba
escenarios = [
    ("A001", 5000, "NORTE"),
    ("A002", "8000", "SUR"),
    ("A003", "inválido", "CENTRO"),
    ("A004", 12000, "NORTE"),
]

resultado = buscar_escenario(escenarios, 10000, "NORTE")
if resultado:
    id_esc, costo, zona = resultado
    print(f"Encontrado: {id_esc} - ${costo} - {zona}")
else:
    print("No encontrado")
