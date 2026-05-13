"""Historial de navegación con adelante/atrás (dos pilas)
Un navegador wev permite ir adelante y atrás en el historial usando dos pilas.

pila_atras: páginas que se puede ir hacia atrás.
pila_adelante: páginas a las que se puede ir hacia adelante después de haber ido atrás.

Reglas:
- Al visitar una nueva página: se agrega a pila_atras, y se limpia pila_adelante.
- Al ir atrás: la página actual se mueve de pila_atras a pila_adelante
- Al ir adelante: la página actual se mueve de pila_adelante a pila_atras

Menú
1. Visitar nueva página.
2. Atrás.
3. Adelante.
4. Ver página actual.
5. Ver historial (atrás y adelante)
6. Salir

Página inicial: inicio"""

historial = []
pila_atras = []
pila_adelante = []
pagina_actual = "Inicio"

while True:
    print("\n--- Menú principal ---")
    print("1. Visitar nueva página")
    print("2. Atrás")
    print("3. Adelante")
    print("4. Ver página actual")
    print("5. Ver historial")
    print("6. Salir")
   
    opcion = input("\nOpción: ")

    if opcion == "1":
        nueva = input("\nNombre: ").strip()
        if nueva:
            historial.append(nueva)
            pila_atras.append(pagina_actual)
            pila_adelante.clear()
            pagina_actual = nueva
            print(f"\nVisitando {nueva}")
            print(f"Página actual: {pagina_actual}")
        else:
            print("No se puede acceder a una página sin nombre")

    elif opcion == "2":
        if pila_atras:
            pila_adelante.append(pagina_actual)
            pagina_actual = pila_atras.pop()
            print(f"Volviendo a: {pagina_actual}")
        else:
            print("No hay páginas atrás")

    elif opcion == "3":
        if pila_adelante:
            pila_atras.append(pagina_actual)
            pagina_actual = pila_adelante.pop()
            print(f"Yendo a {pagina_actual}")
        else:
            print("No hay páginas para avanzar")

    elif opcion == "4":
        print(f"Pagina actual: {pagina_actual}")

    elif opcion == "5":
        print("--- HISTORIAL ---")
        if historial:
            for i, pagina in enumerate(historial, 1):
                print(f"{i}. {pagina}")
        else:
            print("Sin historial.")

    elif opcion == "6":
        print("Has salido!")
        break
    else:
        print("Ingrese una opción válida.")