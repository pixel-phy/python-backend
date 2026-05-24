"""Sistema de amigos en común
Una red solcial necesita recomendar amigos. Cada usuario tiene un conjunto de amigos.
Requisitos:
1. Mostrar los amigos de Ana, Luis, Carlos y Sofía.
2. Encontrar al usuario con más amigos.
3. Mostrar los amigos en común entre Ana y Luis.
4. Recomendar a Ana amigos que no conoce:
- Tomar los amigos de sus amigos.
- Excluir a Ana misma. 
- Excluir a los amigos que Ana ya tiene. 
- Mostrar la lista de recomendaciones ordenada.
5. Encontrar al usuario que tiene más amigos en común con Ana.
6. Mostrar si hay algún amigo que sea común a todos los usuarios."""

amigos_ana = {"Luis", "Carlos", "Sofia", "Juan", "Maria"}
amigos_luis = {"Sofia", "Pedro", "Juan", "Ana", "Diego"}
amigos_carlos = {"Ana", "Luis", "Maria", "Pedro"}
amigos_sofia = {"Luis", "Juan", "Pedro", "Diego", "Ana"}

print("\n--- Amigos de Ana, Luis, Carlos y Sofía ---")
print(f"Amigos Ana: {amigos_ana}")
print(f"Amigos Luis: {amigos_luis}")
print(f"Amigos Carlos: {amigos_carlos}")
print(f"Amigos Sofía: {amigos_sofia}")

print("\n--- Usuarios con más amigos ---")
max_cantidad = len(amigos_ana)
usuario_max = "Ana"

if len(amigos_luis) > max_cantidad:
    max_cantidad = len(amigos_luis)
    usuario_max = "Luis"
elif len(amigos_luis) == max_cantidad:
    max_cantidad = len(amigos_ana)
    usuario_max = "Luis, Ana"
if len(amigos_carlos) > max_cantidad:
    max_cantidad = len(amigos_carlos)
    usuario_max = "Carlos"
elif len(amigos_carlos) == max_cantidad:
    max_cantidad = len(amigos_carlos)
    usuario_max = usuario_max + ", Carlos"

if len(amigos_sofia) > max_cantidad:
    max_cantidad = len(amigos_sofia)
    usuario_max = "Sofia"
elif len(amigos_sofia) == max_cantidad:
    max_cantidad = len(amigos_sofia)
    usuario_max = usuario_max + ", Sofia"

print(f"Usuario(s): {usuario_max} con {max_cantidad} amigos")

print("\n--- Amigos en común entre Ana y Luis ---")
interseccion = amigos_ana & amigos_luis
print(interseccion)

print("\n--- RECOMENDACIÓN A ANA ---")
recomendacion = (amigos_luis | amigos_carlos | amigos_sofia) - amigos_ana - {"Ana"}
print(recomendacion)

print("\n--- Usuario con más amigos en común con Ana ---")
comun_luis = amigos_ana & amigos_luis
comun_carlos = amigos_carlos & amigos_ana
comun_sofia = amigos_ana & amigos_sofia

if (len(comun_luis) > len(comun_carlos)) and (len(comun_luis) > len(comun_sofia)):
    print(f"El usuario que tiene más amigos en común con Ana es Luis. {len(comun_luis)} Amigos en común")
elif (len(comun_carlos) > len(comun_sofia)):
    print(f"El usuario que tiene más amigos en común con Ana es Carlos. {len(comun_carlos)} Amigos en común")
else:
    print(f"El usuario que tiene más amigos en común con Ana es Sofía. {len(comun_sofia)} Amigos en común {comun_sofia}")

print("\n--- Amigo en común de todos ---")
amigo_todos = amigos_ana & amigos_carlos & amigos_luis & amigos_sofia
if amigo_todos:
    print(f"El amigo común de todos es: {amigo_todos}")
else:
    print("No hay nadie que sea amigo de todos los usuarios")