# Contract: API Programática del Núcleo de Conversión

**Feature**: Conversor de temperatura entre Celsius, Fahrenheit y Kelvin
**Branch**: `001-temp-converter`
**Date**: 2026-09-28

Este contrato describe las funciones puras y tipos expuestos por el módulo `conversor.core` para su consumo tanto por la interfaz Tkinter como por la CLI y suites de prueba.

---

## 1. Definición de Constantes y Tipos

```python
ABSOLUTE_ZERO: dict[str, float] = {
    "C": -273.15,
    "F": -459.67,
    "K": 0.0,
}

UNIDADES_VALIDAS: set[str] = {"C", "F", "K"}
```

---

## 2. Firmas de Funciones Principales

### `normalizar_unidad(unidad: str | None) -> str | None`
- **Entrada**: Cadena de texto que representa la unidad (`"c"`, `"CELSIUS"`, `"Fahrenheit (F)"`, etc.).
- **Salida**: `"C"`, `"F"` o `"K"` si es válida; `None` si es desconocida.

### `validar_entrada_temperatura(entrada: str | None) -> tuple[float | None, str | None]`
- **Entrada**: Cadena recibida del usuario.
- **Salida**: `(valor_float, None)` si es válida; `(None, mensaje_error)` si es inválida.
- **Mensajes de error**:
  - `"Ingrese una temperatura"` para entradas nulas, vacías o compuestas solo de espacios.
  - `"Ingrese un número válido"` para cadenas no numéricas.

### `validar_cero_absoluto(valor: float, unidad_origen: str) -> tuple[bool, str | None]`
- **Entrada**: Valor numérico y escala de origen.
- **Salida**: `(True, None)` si `valor >= ABSOLUTE_ZERO[origen]`; `(False, "Temperatura inferior al cero absoluto")` si `valor < ABSOLUTE_ZERO[origen]`.

### `convertir_temperatura(valor: float, origen: str, destino: str) -> float`
- **Entrada**: Valor flotante válido, escala de origen (`"C"`, `"F"`, `"K"`) y destino (`"C"`, `"F"`, `"K"`).
- **Salida**: Valor convertido con máxima precisión sin redondeos intermedios.
- **Excepciones**: Lanza `ValueError` si alguna unidad no pertenece a `UNIDADES_VALIDAS`.

### `formatear_resultado(valor: float, unidad_destino: str) -> str`
- **Entrada**: Valor numérico convertido y escala de destino.
- **Salida**: Cadena con formato `"{valor:.2f} {unidad_destino}"` (normalizando valores `< 1e-9` a `0.0`).

### `procesar_conversion(temp_str: str, origen_str: str, destino_str: str) -> tuple[bool, str]`
- **Función orquestadora de alto nivel**.
- **Salida**: `(True, "212.00 F")` o `(False, "Mensaje de error")`.
