"""Filtrado y transformación con comprensión de listas:
Tienes una lista de precios con descuentos que aplicar, y algunos productos con precio inválido.

precios = [1200, 500, 0, -50, 800, 0, 350]

1. Filtrar los precios válidos (mayores a 0).
2. Aplicar descuento del 10% a los precios mayores a 700.
3. Crear una nueva lista solo con los precios con descuento aplicado (sin modificar la original).
4. Mostrar las tres listas:
- Original
- Filtrados válidos
- Con descuento aplicado """

print("\n=== FILTRADO Y TRANSFORMACIÓN ===\n")
precios = [1200, 500, 0, -50, 800, 0, 350]
filtrados = [p for p in precios if p > 0]
descuentos = [p * 0.9 if p > 700 else p for p in filtrados]
print(f"Lista original: {precios}")
print(f"Filtrados: {filtrados}")
print(f"Descuentos: {descuentos}")