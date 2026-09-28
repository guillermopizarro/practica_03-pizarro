# Technical Research: Conversor de Temperatura (Tkinter & CLI)

**Feature**: Conversor de temperatura entre Celsius, Fahrenheit y Kelvin
**Branch**: `001-temp-converter`
**Date**: 2026-09-28

## Resumen de Decisiones Técnicas

Este documento detalla la investigación técnica, selección de bibliotecas y decisiones de arquitectura para implementar el conversor de temperatura en **Python 3.12** utilizando **uv** como gestor de paquetes y entorno, integrando una **interfaz gráfica en Tkinter** que mantiene el mismo flujo, lógica de validación y comportamiento del Bloque 3.A (además de permitir ejecución por consola/CLI para pruebas y automatización).

---

## 1. Entorno de Ejecución y Gestor de Paquetes (`uv` con Python 3.12)

### Decisión
Configurar el proyecto en la raíz del espacio de trabajo actual (`s4/mi-proyecto-speckit`) utilizando `uv` con Python 3.12 y definiendo un `pyproject.toml` estándar.

### Justificación
- `uv` administra entornos virtuales y dependencias con máxima velocidad y reproducibilidad en Windows.
- Permite invocar la aplicación y las suites de pruebas directamente usando `uv run` sin preocuparse por la activación manual del entorno virtual o políticas de ejecución restringidas de PowerShell (`ExecutionPolicy`).
- Python 3.12 incluye soporte nativo y optimizado para la biblioteca estándar `tkinter`, tipado estático `typing`, y el framework de pruebas `unittest`.

### Alternativas Consideradas
- `pip` + `virtualenv`: Requiere pasos manuales propensos a errores en PowerShell. Rechazado.
- `Poetry`: Mayor lentitud y complejidad para una aplicación de escritorio/CLI ligera.

---

## 2. Diseño de la Interfaz con Tkinter

### Decisión
Implementar una interfaz gráfica con `tkinter` y `tkinter.ttk` (diseño nativo y limpio) que encapsula todos los criterios de aceptación y casos borde del Bloque 3.A:
1. **Componentes visuales**:
   - Campo de entrada (`ttk.Entry`) para ingresar el valor de temperatura.
   - Selectores desplegables (`ttk.Combobox`) o botones de opción para la unidad de origen (`C`, `F`, `K`) y unidad de destino (`C`, `F`, `K`).
   - Botón "Convertir" (`ttk.Button`), vinculado también al evento `<Return>` del teclado.
   - Etiqueta de resultado (`ttk.Label`): Muestra el texto exacto con dos decimales y la unidad de destino (ej. `212.00 F`).
   - Etiqueta de retroalimentación de errores: Muestra mensajes exactos (`Ingrese una temperatura`, `Ingrese un número válido`, `Temperatura inferior al cero absoluto`).
2. **Ciclo de vida y gestión de estado**:
   - Cada intento de conversión limpia inmediatamente cualquier resultado previo antes de validar y calcular.
   - Si la entrada es inválida, se muestra el mensaje de error y el resultado permanece vacío/limpio.
   - El usuario puede realizar conversiones consecutivas ilimitadas sin reiniciar la aplicación.
3. **Modo CLI complementario**:
   - Además de la ventana gráfica de Tkinter (lanzada por defecto al ejecutar sin argumentos o con flag `--gui`), el módulo soportará ejecución por argumentos (`uv run conversor 100 C F`) y modo interactivo de texto para facilitar pruebas automatizadas de integración y scripting.

### Justificación
- Satisface explícitamente el requisito del usuario: "(considerar que la interfaz sea implementada en Tkinter)".
- Mantiene estricta paridad funcional con las reglas del Bloque 3.A.
- `tkinter` viene incluido en la instalación estándar de Python en Windows, no requiere dependencias pesadas de terceros (como PyQt o PySide).

### Alternativas Consideradas
- CustomTkinter: Requiere dependencias externas adicionales que podrían complicar la instalación con `uv` en entornos sin conexión o restringidos. `tkinter` estándar con `ttk` es 100% nativo.

---

## 3. Fórmulas de Conversión y Precisión Aritmética

### Decisión
Utilizar aritmética de punto flotante de doble precisión nativa (`float`) de Python con combinación directa de fórmulas sin redondeos intermedios para conversiones entre Fahrenheit y Kelvin.
- Fórmulas:
  - $C \rightarrow F$: `valor * 9.0 / 5.0 + 32.0`
  - $F \rightarrow C$: `(valor - 32.0) * 5.0 / 9.0`
  - $C \rightarrow K$: `valor + 273.15`
  - $K \rightarrow C$: `valor - 273.15`
  - $F \rightarrow K$: `(valor - 32.0) * 5.0 / 9.0 + 273.15`
  - $K \rightarrow F$: `(valor - 273.15) * 9.0 / 5.0 + 32.0`
- Normalización de cero: Si `abs(valor) < 1e-9`, el valor se establece en `0.0` para evitar `-0.00`.
- Formateo: `f"{valor:.2f} {unidad_destino}"`.

### Justificación
Cumple con las referencias verificables requeridas:
- `0 C -> 32.00 F`
- `32 F -> 0.00 C`
- `0 C -> 273.15 K`
- `273.15 K -> 0.00 C`
- `32 F -> 273.15 K`
- `273.15 K -> 32.00 F`
- `-273.15 C -> 0.00 K`
- `-40 C -> -40.00 F`

---

## 4. Validación de Límites Físicos y Casos Borde

### Decisión
Validación rigurosa antes de cualquier operación aritmética:
1. **Entrada vacía o solo espacios**: Devuelve error `Ingrese una temperatura`.
2. **Entrada no numérica**: Permite comas decimales como separador sustituyéndolas por puntos; si la conversión a float falla, devuelve `Ingrese un número válido`.
3. **Cero absoluto**:
   - $C < -273.15 \rightarrow$ `Temperatura inferior al cero absoluto`
   - $F < -459.67 \rightarrow$ `Temperatura inferior al cero absoluto`
   - $K < 0.0 \rightarrow$ `Temperatura inferior al cero absoluto`
   - Aceptar valores iguales exactos: $-273.15$, $-459.67$, $0.0$.
4. **Misma escala origen y destino**: Conserva el valor numérico, aplica validación de cero absoluto y formatea a dos decimales.

---

## 5. Estrategia de Pruebas

### Decisión
Implementar pruebas exhaustivas con `unittest`:
- `tests/test_converter.py`: Pruebas de todas las fórmulas, límites, casos borde y validaciones de cero absoluto.
- `tests/test_ui_logic.py`: Pruebas de la lógica del controlador de la interfaz (sin depender del display de Tkinter en entornos headless).
