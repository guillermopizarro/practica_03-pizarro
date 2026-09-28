"""Pruebas unitarias para s4/clase-sdd/conversor.py."""

import unittest
from conversor import (
    convertir_temperatura,
    formatear_resultado,
    procesar_conversion,
    validar_cero_absoluto,
    validar_entrada_temperatura,
)


class TestConversorManual(unittest.TestCase):
    def test_referencias_spec(self):
        self.assertEqual(procesar_conversion("0", "C", "F"), (True, "32.00 F"))
        self.assertEqual(procesar_conversion("32", "F", "C"), (True, "0.00 C"))
        self.assertEqual(procesar_conversion("0", "C", "K"), (True, "273.15 K"))
        self.assertEqual(procesar_conversion("273.15", "K", "C"), (True, "0.00 C"))
        self.assertEqual(procesar_conversion("32", "F", "K"), (True, "273.15 K"))
        self.assertEqual(procesar_conversion("273.15", "K", "F"), (True, "32.00 F"))
        self.assertEqual(procesar_conversion("100", "C", "F"), (True, "212.00 F"))

    def test_cero_absoluto_y_limites(self):
        self.assertEqual(procesar_conversion("-273.15", "C", "K"), (True, "0.00 K"))
        self.assertEqual(procesar_conversion("-459.67", "F", "K"), (True, "0.00 K"))
        self.assertEqual(procesar_conversion("0", "K", "C"), (True, "-273.15 C"))
        self.assertEqual(procesar_conversion("-40", "C", "F"), (True, "-40.00 F"))

        self.assertEqual(
            procesar_conversion("-273.16", "C", "K"),
            (False, "Temperatura inferior al cero absoluto"),
        )
        self.assertEqual(
            procesar_conversion("-459.68", "F", "C"),
            (False, "Temperatura inferior al cero absoluto"),
        )
        self.assertEqual(
            procesar_conversion("-0.01", "K", "C"),
            (False, "Temperatura inferior al cero absoluto"),
        )

    def test_casos_borde(self):
        self.assertEqual(procesar_conversion("   ", "C", "F"), (False, "Ingrese una temperatura"))
        self.assertEqual(procesar_conversion("abc", "C", "F"), (False, "Ingrese un número válido"))
        self.assertEqual(procesar_conversion("25", "C", "C"), (True, "25.00 C"))


if __name__ == "__main__":
    unittest.main()
