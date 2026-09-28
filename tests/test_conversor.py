"""Pruebas unitarias para el conversor de temperatura.

Verifica todos los criterios de aceptación y casos borde de spec_manual.md.
"""

import unittest
from practica_03_pizarro.converter import (
    convertir_temperatura,
    formatear_resultado,
    procesar_conversion,
    validar_cero_absoluto,
    validar_entrada_temperatura,
)


class TestConversorTemperatura(unittest.TestCase):
    """Casos de prueba para conversor de temperatura."""

    def test_referencias_verificables(self) -> None:
        """Referencias exactas de la especificación:
        0 C -> 32.00 F
        32 F -> 0.00 C
        0 C -> 273.15 K
        273.15 K -> 0.00 C
        32 F -> 273.15 K
        273.15 K -> 32.00 F
        100 C -> 212.00 F
        """
        # 0 C -> 32.00 F
        exito, res = procesar_conversion("0", "C", "F")
        self.assertTrue(exito)
        self.assertEqual(res, "32.00 F")

        # 32 F -> 0.00 C
        exito, res = procesar_conversion("32", "F", "C")
        self.assertTrue(exito)
        self.assertEqual(res, "0.00 C")

        # 0 C -> 273.15 K
        exito, res = procesar_conversion("0", "C", "K")
        self.assertTrue(exito)
        self.assertEqual(res, "273.15 K")

        # 273.15 K -> 0.00 C
        exito, res = procesar_conversion("273.15", "K", "C")
        self.assertTrue(exito)
        self.assertEqual(res, "0.00 C")

        # 32 F -> 273.15 K
        exito, res = procesar_conversion("32", "F", "K")
        self.assertTrue(exito)
        self.assertEqual(res, "273.15 K")

        # 273.15 K -> 32.00 F
        exito, res = procesar_conversion("273.15", "K", "F")
        self.assertTrue(exito)
        self.assertEqual(res, "32.00 F")

        # 100 C -> 212.00 F
        exito, res = procesar_conversion("100", "C", "F")
        self.assertTrue(exito)
        self.assertEqual(res, "212.00 F")

    def test_limites_y_negativos_validos(self) -> None:
        """Casos borde: aceptar exactamente -273.15 C, -459.67 F y 0 K; -40 C -> -40.00 F."""
        # -273.15 C -> 0.00 K
        exito, res = procesar_conversion("-273.15", "C", "K")
        self.assertTrue(exito)
        self.assertEqual(res, "0.00 K")

        # -459.67 F -> 0.00 K
        exito, res = procesar_conversion("-459.67", "F", "K")
        self.assertTrue(exito)
        self.assertEqual(res, "0.00 K")

        # 0 K -> -273.15 C
        exito, res = procesar_conversion("0", "K", "C")
        self.assertTrue(exito)
        self.assertEqual(res, "-273.15 C")

        # 0 K -> -459.67 F
        exito, res = procesar_conversion("0", "K", "F")
        self.assertTrue(exito)
        self.assertEqual(res, "-459.67 F")

        # -40 C -> -40.00 F
        exito, res = procesar_conversion("-40", "C", "F")
        self.assertTrue(exito)
        self.assertEqual(res, "-40.00 F")

        # -40 F -> -40.00 C
        exito, res = procesar_conversion("-40", "F", "C")
        self.assertTrue(exito)
        self.assertEqual(res, "-40.00 C")

    def test_rechazo_inferior_cero_absoluto(self) -> None:
        """C < -273.15, F < -459.67 o K < 0 deben rechazarse con el mensaje exacto."""
        # Celsius
        exito, msg = procesar_conversion("-273.16", "C", "K")
        self.assertFalse(exito)
        self.assertEqual(msg, "Temperatura inferior al cero absoluto")

        exito, msg = procesar_conversion("-300", "C", "F")
        self.assertFalse(exito)
        self.assertEqual(msg, "Temperatura inferior al cero absoluto")

        # Fahrenheit
        exito, msg = procesar_conversion("-459.68", "F", "C")
        self.assertFalse(exito)
        self.assertEqual(msg, "Temperatura inferior al cero absoluto")

        exito, msg = procesar_conversion("-500", "F", "K")
        self.assertFalse(exito)
        self.assertEqual(msg, "Temperatura inferior al cero absoluto")

        # Kelvin
        exito, msg = procesar_conversion("-0.01", "K", "C")
        self.assertFalse(exito)
        self.assertEqual(msg, "Temperatura inferior al cero absoluto")

        exito, msg = procesar_conversion("-10", "K", "F")
        self.assertFalse(exito)
        self.assertEqual(msg, "Temperatura inferior al cero absoluto")

    def test_misma_unidad_origen_y_destino(self) -> None:
        """Misma unidad conserva el valor válido formateado a dos decimales y valida cero absoluto."""
        exito, res = procesar_conversion("25", "C", "C")
        self.assertTrue(exito)
        self.assertEqual(res, "25.00 C")

        exito, res = procesar_conversion("98.6", "F", "F")
        self.assertTrue(exito)
        self.assertEqual(res, "98.60 F")

        exito, res = procesar_conversion("300", "K", "K")
        self.assertTrue(exito)
        self.assertEqual(res, "300.00 K")

        # Cero absoluto aplica también en misma unidad
        exito, msg = procesar_conversion("-300", "C", "C")
        self.assertFalse(exito)
        self.assertEqual(msg, "Temperatura inferior al cero absoluto")

    def test_entrada_vacia_o_espacios(self) -> None:
        """Entrada vacía o solo espacios -> 'Ingrese una temperatura'."""
        valor, err = validar_entrada_temperatura("")
        self.assertIsNone(valor)
        self.assertEqual(err, "Ingrese una temperatura")

        valor, err = validar_entrada_temperatura("   ")
        self.assertIsNone(valor)
        self.assertEqual(err, "Ingrese una temperatura")

        exito, msg = procesar_conversion("   ", "C", "F")
        self.assertFalse(exito)
        self.assertEqual(msg, "Ingrese una temperatura")

    def test_texto_no_numerico(self) -> None:
        """Texto no numérico como 'abc' -> 'Ingrese un número válido'."""
        valor, err = validar_entrada_temperatura("abc")
        self.assertIsNone(valor)
        self.assertEqual(err, "Ingrese un número válido")

        exito, msg = procesar_conversion("abc", "C", "F")
        self.assertFalse(exito)
        self.assertEqual(msg, "Ingrese un número válido")

    def test_caso_no_contemplado_minusculas_y_nombres(self) -> None:
        """Casos no contemplados en la spec: minúsculas, nombres completos y espacios extra."""
        exito, res = procesar_conversion(" 100 ", "c", "f")
        self.assertTrue(exito)
        self.assertEqual(res, "212.00 F")

        exito, res = procesar_conversion("0", "celsius", "kelvin")
        self.assertTrue(exito)
        self.assertEqual(res, "273.15 K")

        # Unidad no válida
        exito, msg = procesar_conversion("100", "X", "C")
        self.assertFalse(exito)
        self.assertIn("no válida", msg)


if __name__ == "__main__":
    unittest.main()
