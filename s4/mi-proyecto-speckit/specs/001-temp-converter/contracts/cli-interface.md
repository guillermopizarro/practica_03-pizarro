# Contract: Interfaz de Línea de Comandos (CLI)

**Feature**: Conversor de temperatura entre Celsius, Fahrenheit y Kelvin
**Branch**: `001-temp-converter`
**Date**: 2026-09-28

Este contrato describe la interfaz de línea de comandos para la aplicación, garantizando total paridad con el comportamiento del Bloque 3.A.

---

## 1. Modo Interactivo (Default)

### Invocación
```powershell
uv run python -m conversor.cli
# O mediante el script configurado en pyproject.toml:
uv run conversor
```

### Flujo de Interacción Estándar

```text
=== Conversor de Temperatura ===
Unidades permitidas: Celsius (C), Fahrenheit (F), Kelvin (K)
Escriba 'salir' para terminar el programa.

Ingrese la temperatura: 100
Ingrese la unidad de origen (C, F, K): C
Ingrese la unidad de destino (C, F, K): F
Resultado: 212.00 F

Ingrese la temperatura: 
```

### Flujo Rápido (Una sola línea)
El usuario puede ingresar temperatura, origen y destino en un solo renglón separados por espacios:
```text
Ingrese la temperatura: 100 C F
Resultado: 212.00 F
```

### Manejo de Salida del Programa
Comandos aceptados para finalizar la ejecución: `salir`, `exit`, `quit`, `q` (insensible a mayúsculas/minúsculas).
Salida en consola:
```text
Programa finalizado.
```

---

## 2. Modo por Argumentos CLI

### Invocación
```powershell
uv run conversor <temperatura> <origen> <destino>
```

### Contrato de Respuestas por Argumentos

| Comando de Ejemplo | Salida Estándar (`stdout`) | Código de Salida |
|---|---|---|
| `uv run conversor 100 C F` | `Resultado: 212.00 F` | `0` |
| `uv run conversor 0 C K` | `Resultado: 273.15 K` | `0` |
| `uv run conversor 32 F K` | `Resultado: 273.15 K` | `0` |
| `uv run conversor -273.15 C K` | `Resultado: 0.00 K` | `0` |
| `uv run conversor -300 C F` | `Temperatura inferior al cero absoluto` | `0` |
| `uv run conversor abc C F` | `Ingrese un número válido` | `0` |
| `uv run conversor " " C F` | `Ingrese una temperatura` | `0` |

---

## 3. Mensajes de Error y Validación

| Condición | Mensaje Mostrado | Presenta Resultado |
|---|---|---|
| Entrada vacía o solo espacios | `Ingrese una temperatura` | No |
| Entrada no numérica (ej. `abc`, `12..3`) | `Ingrese un número válido` | No |
| Unidad de origen desconocida | `Unidad de origen no válida. Ingrese C, F o K.` | No |
| Unidad de destino desconocida | `Unidad de destino no válida. Ingrese C, F o K.` | No |
| Valor inferior a -273.15 C, -459.67 F o 0 K | `Temperatura inferior al cero absoluto` | No |
