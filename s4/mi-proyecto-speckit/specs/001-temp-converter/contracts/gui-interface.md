# Contract: Interfaz Gráfica de Usuario (Tkinter)

**Feature**: Conversor de temperatura entre Celsius, Fahrenheit y Kelvin
**Branch**: `001-temp-converter`
**Date**: 2026-09-28

Este contrato describe los componentes, eventos, validaciones y diseño visual de la interfaz de usuario implementada en Tkinter.

---

## 1. Ventana Principal

- **Título de la ventana**: `Conversor de Temperatura`
- **Dimensiones por defecto**: 400x320 píxeles (redimensionable o centrada).
- **Tema/Estilo**: `ttk` nativo para integración visual con el sistema operativo Windows.

---

## 2. Componentes y Controles

| ID del Componente | Widget | Etiqueta / Texto | Descripción / Valores |
|---|---|---|---|
| `lbl_title` | `ttk.Label` | `Conversor de Temperatura` | Título encabezado destacado |
| `lbl_temp` | `ttk.Label` | `Temperatura:` | Etiqueta del campo de entrada |
| `entry_temp` | `ttk.Entry` | - | Campo de texto para ingresar el valor numérico |
| `lbl_source` | `ttk.Label` | `Unidad de origen:` | Etiqueta del selector de origen |
| `combo_source` | `ttk.Combobox` | `Celsius (C)` | Opciones: `Celsius (C)`, `Fahrenheit (F)`, `Kelvin (K)` |
| `lbl_target` | `ttk.Label` | `Unidad de destino:` | Etiqueta del selector de destino |
| `combo_target` | `ttk.Combobox` | `Fahrenheit (F)` | Opciones: `Celsius (C)`, `Fahrenheit (F)`, `Kelvin (K)` |
| `btn_convert` | `ttk.Button` | `Convertir` | Dispara el cálculo y validación |
| `lbl_result` | `ttk.Label` | - | Muestra el resultado (ej. `Resultado: 212.00 F`) con estilo resaltado |
| `lbl_error` | `ttk.Label` | - | Muestra mensajes de error en color rojo |

---

## 3. Comportamiento de Eventos

1. **Clic en `btn_convert` o pulsar `<Return>` en `entry_temp`**:
   - Se ejecuta el proceso de validación y conversión.
2. **Retroalimentación visual**:
   - **Caso exitoso**:
     - `lbl_error`: Vacío (`""`).
     - `lbl_result`: Texto con formato `Resultado: {valor:.2f} {unidad_destino}` (ejemplo: `Resultado: 212.00 F`).
   - **Caso de error**:
     - `lbl_result`: Vacío (`""`) (garantiza que resultados previos no persistan).
     - `lbl_error`: Mensaje exacto de validación:
       - Si campo vacío o espacios: `"Ingrese una temperatura"`.
       - Si texto no numérico: `"Ingrese un número válido"`.
       - Si valor < cero absoluto: `"Temperatura inferior al cero absoluto"`.
3. **Conversiones sucesivas**:
   - El usuario puede modificar el texto de entrada o cambiar unidades en los combos y volver a pulsar "Convertir" tantas veces como desee sin reiniciar la aplicación.
