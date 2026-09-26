# Especificación manual — Conversor de temperatura

## Objetivo
Convertir una temperatura entre Celsius, Fahrenheit y Kelvin para consultar su equivalencia en otra escala.

## Criterios de aceptación
- [ ] Permite ingresar una temperatura y seleccionar las unidades de origen y destino entre Celsius (C), Fahrenheit (F) y Kelvin (K).
- [ ] Convierte entre las tres escalas usando C = (F - 32) × 5/9, F = C × 9/5 + 32, K = C + 273.15 y C = K - 273.15; para F ↔ K combina esas fórmulas sin redondeos intermedios. Referencias verificables: 0 C → 32.00 F; 32 F → 0.00 C; 0 C → 273.15 K; 273.15 K → 0.00 C; 32 F → 273.15 K; 273.15 K → 32.00 F.
- [ ] Muestra cada resultado válido con exactamente dos decimales y la unidad de destino; por ejemplo, 100 C → 212.00 F.
- [ ] Rechaza entradas inferiores al cero absoluto según la unidad de origen: C < -273.15, F < -459.67 o K < 0. Muestra «Temperatura inferior al cero absoluto» y no presenta un resultado de conversión.
- [ ] Después de una conversión o un error, permite realizar otra conversión sin reiniciar el programa y sin conservar un resultado anterior como si correspondiera a la entrada actual.

## Casos borde
- Entrada vacía o formada únicamente por espacios → mostrar «Ingrese una temperatura» y no convertir.
- Texto no numérico, como «abc» → mostrar «Ingrese un número válido», sin una excepción sin controlar y sin presentar un resultado.
- Límite y negativos válidos → aceptar exactamente -273.15 C, -459.67 F y 0 K; -273.15 C → 0.00 K. Aceptar también -40 C → -40.00 F.
- Misma unidad de origen y destino → conservar el valor si es válido y aplicar el formato de dos decimales; por ejemplo, 25 C → 25.00 C. Mantener la validación del cero absoluto.
