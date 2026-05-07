"""Sistema de películas
Un sistema de gestión necesita ordenar y filtrar
peliculas = [
    {"titulo": "Inception", "anio":2010, "puntaje": 8.8},
    {"titulo": "The Matrix", "anio": 1999, "puntaje": 8.7},
    {"titulo": "Interestellar", "anio": 2014, "puntaje": 8.6},
    {"titulo": "Parasite", "anio": 2019, "puntaje": 8.6},
    {"titulo": "Gladiato", "anio": 2000, "puntaje": 8.5}
    ]
1. Mostrar la lista original.
2. Ordenar por año (de más antigua a más nueva).
3. Ordenar por puntaje (de mayor a menor).
4. Ordenar por título alfabético.
5. Mostrar solo las películas con puntaje mayor a 8.6"""

peliculas = [
    {"titulo": "Inception", "anio": 2010, "puntaje": 8.8},
    {"titulo": "The Matrix", "anio": 1999, "puntaje": 8.7},
    {"titulo": "Interestellar", "anio": 2014, "puntaje": 8.6},
    {"titulo": "Parasite", "anio": 2019, "puntaje": 8.6},
    {"titulo": "Gladiator", "anio": 2000, "puntaje": 8.5}
]
# Mostramos la lista
print("\nLista original:")
for p in peliculas:
    print(f"{p}")

# Ordenamos por año (de más antigua a más nueva)
peliculas.sort(key=lambda x : x["anio"])
print("\nDe más antigua a más nueva:")
for p in peliculas:
    print(f" {p["anio"]}: {p["titulo"]}")

# Ordenamos por puntaje (de  mayor a menor)
peliculas.sort(key=lambda x: x["puntaje"])
print(f"\nDe mayor puntaje a menor:")
for p in peliculas:
    print(f"{p['puntaje']}: {p['titulo']}")

# Ordenamos por título
peliculas.sort(key=lambda x : x["titulo"])
print(f"\nOrdenadas por título: ")
for p in peliculas:
    print(f"{p['titulo']}")

# Mostramos solo las películas con puntaje mayor a 8.6
filtrada = [p for p in peliculas if p["puntaje"] > 8.6]
print(f"\nPelículas con puntaje > 8.6:")
for p in filtrada:
    print(f" {p["titulo"]} - {p["puntaje"]}")