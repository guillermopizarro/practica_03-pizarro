# Guía Rápida de Ejecución: Conversor de Temperatura (Windows con PowerShell)

**Feature**: Conversor de temperatura entre Celsius, Fahrenheit y Kelvin
**Branch**: `001-temp-converter`
**Date**: 2026-09-28

Esta guía detalla los pasos para validar y ejecutar la aplicación del conversor de temperatura (tanto en interfaz gráfica **Tkinter** como en **CLI**) en **Windows** utilizando **PowerShell** y **uv**.

---

## 1. Requisitos Previos

1. **Sistema Operativo**: Windows 10 / 11 con PowerShell.
2. **Python**: Python 3.12 (gestionado automáticamente por `uv`).
3. **uv**: Herramienta de gestión de entornos y paquetes de Python instalada.
   - Para verificar en PowerShell:
     ```powershell
     uv --version
     ```

---

## 2. Ubicación del Proyecto

Abrir PowerShell y posicionarse en la carpeta del proyecto actual:
```powershell
cd C:\Users\KarinaAnabellaAscenc\Documents\GitHub\practica_03-pizarro\s4\mi-proyecto-speckit
```

---

## 3. Ejecución de la Interfaz Gráfica (Tkinter)

Para abrir la ventana de usuario interactiva implementada en Tkinter:

```powershell
uv run python -m conversor.gui
```
O directamente con el ejecutable del proyecto:
```powershell
uv run conversor
```

### Escenarios de Prueba en la Interfaz Gráfica:
1. **Conversión 100 C a Fahrenheit**:
   - Ingresar `100` en el campo *Temperatura*.
   - Seleccionar *Celsius (C)* en origen y *Fahrenheit (F)* en destino.
   - Hacer clic en **Convertir** (o presionar `Enter`).
   - Resultado esperado: `Resultado: 212.00 F`.
2. **Validación de Cero Absoluto**:
   - Ingresar `-300` con unidad origen *Celsius (C)*.
   - Hacer clic en **Convertir**.
   - Resultado esperado: Mensaje rojo `Temperatura inferior al cero absoluto`. El resultado anterior se limpia y no se muestra ningún cálculo.
3. **Validación de Texto No Numérico**:
   - Ingresar `abc`.
   - Hacer clic en **Convertir**.
   - Resultado esperado: Mensaje `Ingrese un número válido`.
4. **Validación de Entrada Vacía**:
   - Dejar el campo vacío o con espacios y hacer clic en **Convertir**.
   - Resultado esperado: Mensaje `Ingrese una temperatura`.
5. **Conversión de Escala Idéntica**:
   - Ingresar `25` de *Celsius (C)* a *Celsius (C)*.
   - Resultado esperado: `Resultado: 25.00 C`.

---

## 4. Ejecución en Modo Consola (CLI)

También es posible ejecutar conversiones directas desde la terminal de PowerShell:

### Modo directo por argumentos:
```powershell
uv run python -m conversor.cli 100 C F
```
Salida esperada:
```text
Resultado: 212.00 F
```

### Modo interactivo de consola:
```powershell
uv run python -m conversor.cli
```
Salida esperada:
```text
=== Conversor de Temperatura ===
Unidades permitidas: Celsius (C), Fahrenheit (F), Kelvin (K)
Escriba 'salir' para terminar el programa.

Ingrese la temperatura: 
```

---

## 5. Ejecución de la Suite de Pruebas Automatizadas

Para ejecutar todas las pruebas unitarias que validan las fórmulas físicas, referencias verificables y casos borde:

```powershell
uv run python -m unittest discover -s tests -p "test_*.py" -v
```

Todas las pruebas deben concluir con `OK`.
