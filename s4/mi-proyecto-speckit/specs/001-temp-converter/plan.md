# Implementation Plan: Conversor de Temperatura (Tkinter & CLI)

**Branch**: `001-temp-converter` | **Date**: 2026-09-28 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/001-temp-converter/spec.md`

## Summary

Implementar un conversor de temperatura bidireccional entre las escalas Celsius (C), Fahrenheit (F) y Kelvin (K) desarrollado en **Python 3.12** y gestionado con **uv**. La solución ofrece una interfaz gráfica moderna e interactiva implementada en **Tkinter**, manteniendo estricta fidelidad funcional con la lógica del Bloque 3.A (validación rigurosa del cero absoluto, soporte de límites exactos, formateo con dos decimales y descarte de estados erróneos previos), complementada con una interfaz CLI ejecutable desde PowerShell.

## Technical Context

**Language/Version**: Python 3.12 (gestionado con `uv 0.12.x`)

**Primary Dependencies**: Ninguna dependencia pesada externa. Utiliza módulos nativos de la biblioteca estándar de Python: `tkinter` (y `ttk` para la GUI), `typing` y `sys`.

**Storage**: N/A (operación en memoria sin persistencia en base de datos).

**Testing**: Módulo estándar `unittest` ejecutado a través de `uv run python -m unittest`.

**Target Platform**: Windows 10 / 11 (PowerShell) y multiplataforma.

**Project Type**: Aplicación de escritorio gráfica (`tkinter`) + Utilidad de consola CLI.

**Performance Goals**: Tiempo de respuesta de conversión inmediato (< 10 ms); arranque rápido de la GUI con `uv`.

**Constraints**:
- Cumplimiento estricto de las fórmulas matemáticas sin redondeos intermedios en $F \leftrightarrow K$.
- Formato exacto de dos cifras decimales con la unidad de destino (ej. `212.00 F`).
- Rechazo estricto de valores inferiores al cero absoluto ($-273.15$ C, $-459.67$ F, $0$ K).
- Aislamiento de resultados anteriores ante nuevos errores en la GUI y CLI.

**Scale/Scope**: Módulo independiente autocontenido en el proyecto actual `s4/mi-proyecto-speckit`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Principle 1 (Library-First / Core Separation)**: ✅ PASA. La lógica central de conversión y validaciones reside en `src/conversor/core.py`, desacoplada por completo de la interfaz de usuario.
- **Principle 2 (Dual Interface - GUI + CLI)**: ✅ PASA. Se provee tanto la interfaz gráfica en Tkinter (`src/conversor/gui.py`) como la interfaz de consola (`src/conversor/cli.py`).
- **Principle 3 (Test-First & Reproducibility)**: ✅ PASA. Casos de prueba exhaustivos en `tests/` cubriendo el 100% de los criterios de aceptación y referencias verificables.
- **Principle 4 (Simplicity / YAGNI)**: ✅ PASA. Solución limpia sin dependencias externas innecesarias, aprovechando la biblioteca estándar de Python y `uv`.

## Project Structure

### Documentation (this feature)

```text
specs/001-temp-converter/
├── spec.md                  # Especificación funcional validada
├── plan.md                  # Este archivo (plan de implementación)
├── research.md              # Investigación técnica y decisiones de diseño
├── data-model.md            # Modelo de datos y máquina de estados
├── quickstart.md            # Guía de ejecución en Windows con PowerShell y uv
├── contracts/               # Contratos de interfaces
│   ├── gui-interface.md     # Contrato de la interfaz Tkinter
│   ├── cli-interface.md     # Contrato de la interfaz de consola
│   └── converter-api.md     # Contrato de la API de funciones en Python
└── checklists/
    └── requirements.md      # Lista de verificación de calidad del spec
```

### Source Code (project root: `s4/mi-proyecto-speckit`)

```text
pyproject.toml               # Configuración del paquete y scripts con uv
src/
└── conversor/
    ├── __init__.py          # Exportación de tipos y funciones principales
    ├── core.py              # Lógica pura: fórmulas, cero absoluto, formateo
    ├── gui.py               # Interfaz gráfica interactiva con Tkinter y ttk
    └── cli.py               # Interfaz CLI interactiva y por argumentos
tests/
    ├── __init__.py
    ├── test_converter.py    # Pruebas unitarias de fórmulas y casos borde
    └── test_ui_logic.py     # Pruebas de integración de validaciones y flujos
```

**Structure Decision**: Arquitectura modular simple con separación limpia entre núcleo de negocio (`core.py`), interfaz gráfica (`gui.py`) e interfaz de línea de comandos (`cli.py`).

## Complexity Tracking

*No hay violaciones a la constitución ni complejidades injustificadas.*
