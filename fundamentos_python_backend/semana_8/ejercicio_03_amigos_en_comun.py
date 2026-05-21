"""Problema de conjuntos - Amigos en común (red social)
Una red social necesita recomendar amigos en común entre dos usuarios.
Requisitos:
1. Mostrar los amigos de Ana y de Luis.
2. Mostrar los amigos en común entre Ana y Luis.
3. Mostrar los amigos que tiene Ana pero no Luis.
4. Mostrar los amigos que tiene Luis pero no Ana.
5. Mostrar los amigos que tiene Ana o Luis.
6. Mostrar los amigos que tiene Ana o Luis, pero no ambos.
7. Recomendar a Ana amigos que no conoce:
- Tomar los amigos de Luis
- Quitar a Ana misma
- Quitar a los amigos que Ana ya tiene
- Mostrar la lista de recomendaciones
8. Verificar si Ana y Carlos tienen amigos en común."""

amigos_ana = {"Luis", "Carlos", "Sofia", "Juan", "Maria"}
amigos_luis = {"Sofia", "Pedro", "Juan", "Ana", "Diego"}
amigos_carlos = {"Ana", "Luis", "Maria", "Pedro"}

print("\n--- Amigos Ana ---")
print(amigos_ana)
print("\n--- Amigos Luis ---")
print(amigos_luis)

# Amigos en común aplicamos intersección
print("\n--- Amigos en común ---")
amigos_comun = amigos_ana & amigos_luis
print(amigos_comun)

# Amigos que tiene Ana pero no Luis
print("\n--- Amigos de Ana que no tiene Luis ---")
diferencia = amigos_ana - amigos_luis
print(diferencia)

# Amigos que tiene Luis pero no Ana
print("\n--- Amigos que tiene Luis pero no Ana ---")
diferencia2 = amigos_luis - amigos_ana
print(diferencia2)

# Los amigos de ambos
print("\n--- Amigos de Ana o Luis ---")
print(amigos_ana | amigos_luis)

# Amigos que tiene Ana o Luis
print("\n--- Amigos que tiene Ana, pero no ambos ---")
dif_simetrica = amigos_luis ^ amigos_ana
print(dif_simetrica)

if "Ana" in amigos_luis:
    amigos_luis.remove("Ana")
    print("Se eliminó a Ana para la recomendación.")
else:
    print("Ana no está en los amigos de Luis")

recomendacion = amigos_luis - amigos_ana
print("\n--- RECOMENDACION ---")
print(recomendacion)

print("\n--- Amigos en común Carlos y Ana ---")
if amigos_ana.isdisjoint(amigos_carlos):
    print("No, Ana y Carlos no tienen amigos en común")
else:
    print("Sí, Ana y Carlos sí tienen amigos en común")