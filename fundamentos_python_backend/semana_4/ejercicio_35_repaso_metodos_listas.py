"""Dada la lista tareas = ["estudiar", "comprar", "limpiar", "cocinar"], realiza las siguientes operaciones:
1. Agrega "leer" al final.
2. Inserta "correr" en la posición 2. 
3. Elimina "limpiar". 
4. Elimina el último elemento de la lista. 
5. Muestra la lista final. """

tareas = ["estudiar", "comprar", "limpiar", "cocinar"]
print(f"\nLista original: {tareas}")
tareas.append("leer")
print(f"Después de agregar leer: {tareas}")
tareas.insert(2, "correr")
print(f"Después de insertar correr: {tareas}")
tareas.remove("limpiar")
print(f"Después de eliminar limpiar: {tareas}")
eliminado = tareas.pop()
print(f"Después de eliminar: {eliminado}")
print(f"Lista final: {tareas}")