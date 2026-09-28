"""Paquete conversor de temperatura entre Celsius, Fahrenheit y Kelvin."""

from .core import (
    ABSOLUTE_ZERO,
    UNIDADES_VALIDAS,
    convertir_temperatura,
    formatear_resultado,
    normalizar_unidad,
    procesar_conversion,
    validar_cero_absoluto,
    validar_entrada_temperatura,
)

__all__ = [
    "ABSOLUTE_ZERO",
    "UNIDADES_VALIDAS",
    "convertir_temperatura",
    "formatear_resultado",
    "normalizar_unidad",
    "procesar_conversion",
    "validar_cero_absoluto",
    "validar_entrada_temperatura",
]
