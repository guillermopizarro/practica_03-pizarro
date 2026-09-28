# Conversor de Temperatura (Tkinter & CLI)

Conversor de temperatura entre Celsius (C), Fahrenheit (F) y Kelvin (K) desarrollado en Python 3.12 con soporte para interfaz gráfica Tkinter e interfaz de línea de comandos (CLI).

## Requisitos
- Python >= 3.12
- uv

## Cómo ejecutar

### Interfaz Gráfica (Tkinter)
```powershell
uv run conversor
# o:
uv run python -m conversor.gui
```

### Línea de Comandos (CLI)
```powershell
# Modo directo por argumentos:
uv run python -m conversor.cli 100 C F

# Modo interactivo:
uv run python -m conversor.cli
```

### Pruebas Automatizadas
```powershell
uv run python -m unittest discover -s tests -p "test_*.py" -v
```
