# 📚 Semana 12: Archivos

## 🎯 Objetivo de la semana

Aprender a manejar archivos en Python: abrir, leer, escribir y procesar diferentes formatos (texto plano, CSV). Estas habilidades son fundamentales para:
- Leer archivos de configuración
- Procesar logs y bitácoras
- Exportar/importar datos en formato CSV
- Crear sistemas de registro de datos

---

## 📂 Estructura de aprendizaje

[Día 1: Apertura & Encoding] → [Día 2: Lectura Eficiente] → [Día 3: Escritura & Descarga]
│
[Día 6: Ejercicios Integradores] ← [Día 5: Datos en CSV] ← [Día 4: Context Managers & Errores]
│
[Día 7: PROYECTO FINAL]


---

## 📂 Estructura de la carpeta
semana_12_archivos/
├── README.md
├── dia1_apertura_encoding.py
├── dia2_lectura_eficiente.py
├── dia3_escritura_descarga.py
├── dia4_context_managers_errores.py
├── dia5_datos_csv.py
├── dia6_ejercicios_integradores.py
└── proyecto_final.py


---

## 📋 Contenido de la semana

| Día | Tema | Conceptos clave |
|-----|------|-----------------|
| **1** | Apertura & Encoding | `open()`, modos (`r`, `w`, `a`, `x`, `r+`, `w+`, `a+`,), encoding (`utf-8`, `latin-1`), errores de encoding |
| **2** | Lectura Eficiente | `read()`, `readline()`, `readlines()`, iteración con `for`, archivos grandes |
| **3** | Escritura & Descarga | `write()`, `writelines()`, `flush()`, buffering, simulación de descarga |
| **4** | Context Managers & Errores | `with open() as archivo`, `FileNotFoundError`, `PermissionError` |
| **5** | Datos en CSV | `csv.reader()`, `csv.writer()`, `DictReader()`, `DictWriter()` |
| **6** | Ejercicios Integradores | Combinar lectura, escritura y transformación de datos |
| **7** | PROYECTO FINAL | Sistema de registro de datos con exportación CSV |

---

## 🔍 Ejemplos rápidos

### Apertura básica
```python
archivo = open("datos.txt", "r", encoding="utf-8")
contenido = archivo.read()
archivo.close()
```

## 🔍 Context manager (reocmendado)

```python
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
# El archivo se cierra automáticamente

```

## 🔍 Leer CSV
```python
import csv
with open("datos.csv", "r") as f:
    lector = csv.reader(f)
    for fila in lector:
        print(fila)
```

## 🔍 Escribir CSV
```python
with open("salida.csv", "w") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nombre", "edad"])
    escritor.writerow(["Ana", 25])
```
```
