"""Ejercicio 5: Modificar elementos en diccionarios anidados

Dada la base de datos con múltiples conexiones:
    1. Cambia el "pool_size" de "produccion" a 20.
    2. Agrega una clave "timeout" con valor 30 dentro de "testing".
    3. Imprime solo el "host" de "produccion"
    4. Imprime solo el "database" de "testing". """

db_config = {
        "produccion": {
            "host": "db.prod.com",
            "port": 5432,
            "database": "tienda_prod",
            "pool_size": 10
        },
        "testing": {
            "host": "db.test.com",
            "port": 5432,
            "database": "tienda_test",
            "pool_size": 2
        }
    }

db_config["produccion"]["pool_size"] = 20
if "timeout" not in db_config["testing"]:
    db_config["testing"]["timeout"] = 30

print(db_config["produccion"]["host"])
print(db_config["testing"]["database"])
