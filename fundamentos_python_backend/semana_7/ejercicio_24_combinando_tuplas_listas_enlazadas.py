"""Combinando tuplas y listas enlazadas:
Una lita de reproducción de música donde cada canción es una tupla (id, título, artista, duracion). La lista enlazada
mantiene el orden de reproducción.
Lista inicial: 
(1, "Bohemian Rhapsody", "Queen", 354)
(2, "Imagine", "John Lennon", 183) 
(3, "Billien Jean", "Michael Jackson", 294)
Requisitos:
1. Crear una lista enlazada con las tres canciones.
2. Mostrar todas las canciones en orden (recorrer la lista).
3. Buscar canción por título y mostrar su artista y duración.
4. Insertar una nueva canción al inicio de la lista:
(4, "Hey Jude", "The Beatles", 431)
5. Eliminar la canción con título "Imagine".
6. Mostrar la lista actualizada."""

class ListaReproduccion:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None

cancion1 = ListaReproduccion((1, "Bohemian Rhapsody", "Queen", 354))
cancion2 = ListaReproduccion((2, "Imagine", "John Lennon", 183))
cancion3 = ListaReproduccion((3, "Billie Jean", "Michael Jackson", 294))

cancion1.siguiente = cancion2
cancion2.siguiente = cancion3
cancion3.siguiente = None

actual = cancion1
while actual is not None:
    print(actual.cancion)
    actual = actual.siguiente

titulo_buscar = input("\nTítulo a buscar: ").strip().title()

actual = cancion1
posicion = 1
while actual is not None:
    if actual.cancion[1] ==titulo_buscar:
        print(f"Artista: {actual.cancion[2]} - Duración: {actual.cancion[3]} s")
        break
    actual = actual.siguiente
    posicion += 1
else:
    print(f"'{titulo_buscar}' No econtrado")

# Insertar al inicio
nueva_cancion = ListaReproduccion((4, "Hey Jude", "The Beatles", 431))
nueva_cancion.siguiente = cancion1
cancion1 = nueva_cancion

# Eliminamos la canción con título Imagine
eliminar = "Imagine"
print(f"\nEliminando la canción {eliminar}...")
if cancion1.cancion[1] == eliminar:
    cancion1 = cancion1.siguiente
    print(f"\nCanción '{eliminar}' eliminada con éxito")
else:
    actual = cancion1
    while actual.siguiente is not None and actual.siguiente.cancion[1] != eliminar:
        actual = actual.siguiente
    
    if actual.siguiente is not None:
        actual.siguiente = actual.siguiente.siguiente
        print(f"\nCanción '{eliminar}' eliminada con éxito")
    else:
        print(f"\nCanción '{eliminar}' no encontrada")

print("\n--- LISTA ACTUALIZADA ---\n")
actual = cancion1
while actual:
    print(actual.cancion)
    actual = actual.siguiente