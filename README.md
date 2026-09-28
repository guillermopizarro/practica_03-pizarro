# Práctica 03 — Conversor de Temperatura

Implementación de la **Práctica 03** (Bloque 3.A: SDD — Spec a mano) para la conversión de temperatura entre Celsius (C), Fahrenheit (F) y Kelvin (K).

## Objetivo
Convertir una temperatura entre Celsius, Fahrenheit y Kelvin para consultar su equivalencia en otra escala.

## Criterios de Aceptación Implementados
- [x] Entrada de temperatura y selección de unidades origen y destino (C, F, K).
- [x] Conversión exacta usando las fórmulas estándar sin redondeos intermedios:
  - $C = (F - 32) \times \frac{5}{9}$
  - $F = C \times \frac{9}{5} + 32$
  - $K = C + 273.15$
  - $C = K - 273.15$
  - $F \leftrightarrow K$: combinación directa sin redondeos intermedios.
- [x] Formato de resultado con exactamente dos decimales y la unidad de destino (ej. `212.00 F`).
- [x] Rechazo de temperaturas inferiores al cero absoluto según la unidad de origen:
  - Celsius: $C < -273.15$
  - Fahrenheit: $F < -459.67$
  - Kelvin: $K < 0$
  - Mensaje mostrado: `Temperatura inferior al cero absoluto`.
- [x] Bucle interactivo continuo que no conserva estados erróneos ni resultados previos entre ejecuciones.

## Casos Borde Contemplados
- **Entrada vacía o solo espacios:** muestra `Ingrese una temperatura` y solicita nuevo valor.
- **Entrada no numérica (ej. `abc`):** muestra `Ingrese un número válido` sin excepciones no controladas.
- **Límites exactos y negativos:** acepta `-273.15 C` ($\rightarrow$ `0.00 K`), `-459.67 F` ($\rightarrow$ `0.00 K`), `0 K` ($\rightarrow$ `-273.15 C`), `-40 C` ($\rightarrow$ `-40.00 F`).
- **Misma unidad origen y destino:** conserva el valor formateado a dos decimales (`25 C` $\rightarrow$ `25.00 C`) validando el cero absoluto.
- **Casos no contemplados manejados:** tolerancia a minúsculas (`c`, `f`, `k`), tolerancia a nombres de escala (`celsius`, `fahrenheit`, `kelvin`), y entrada rápida en una sola línea (ej. `100 C F`).

## Cómo ejecutar

### Modo interactivo
```bash
uv run practica-03-pizarro
```
o directamente desde `s4/clase-sdd/`:
```bash
python s4/clase-sdd/conversor.py
```

### Modo por argumentos
```bash
uv run practica-03-pizarro 100 C F
```
Salida:
```
Resultado: 212.00 F
```

## Pruebas automatizadas

Ejecutar la suite completa de pruebas unitarias:
```bash
uv run python -m unittest discover -s tests -p "test_*.py"
```
O dentro de `s4/clase-sdd`:
```bash
uv run python s4/clase-sdd/test_conversor.py
```
