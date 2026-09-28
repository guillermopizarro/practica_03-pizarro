"""Pruebas unitarias para las funciones de conversión de temperatura."""

import unittest
from conversor.core import (
    ABSOLUTE_ZERO,
    UNIDADES_VALIDAS,
    convertir_temperatura,
    formatear_resultado,
    normalizar_unidad,
    validar_cero_absoluto,
)


class TestFoundational(unittest.TestCase):
    """Verificación de constantes y funciones fundacionales."""

    def test_constantes_cero_absoluto(self):
        self.assertEqual(ABSOLUTE_ZERO["C"], -273.15)
        self.assertEqual(ABSOLUTE_ZERO["F"], -459.67)
        self.assertEqual(ABSOLUTE_ZERO["K"], 0.0)

    def test_unidades_validas(self):
        self.assertEqual(UNIDADES_VALIDAS, {"C", "F", "K"})

    def test_normalizar_unidad_simbolos(self):
        self.assertEqual(normalizar_unidad("c"), "C")
        self.assertEqual(normalizar_unidad("C"), "C")
        self.assertEqual(normalizar_unidad("f"), "F")
        self.assertEqual(normalizar_unidad("k"), "K")

    def test_normalizar_unidad_nombres_largos(self):
        self.assertEqual(normalizar_unidad("Celsius"), "C")
        self.assertEqual(normalizar_unidad("celsius"), "C")
        self.assertEqual(normalizar_unidad("Celsius (C)"), "C")
        self.assertEqual(normalizar_unidad("FAHRENHEIT"), "F")
        self.assertEqual(normalizar_unidad("Kelvin (K)"), "K")

    def test_normalizar_unidad_invalida(self):
        self.assertIsNone(normalizar_unidad(None))
        self.assertIsNone(normalizar_unidad(""))
        self.assertIsNone(normalizar_unidad("X"))
        self.assertIsNone(normalizar_unidad("Rankine"))


class TestUserStory1Conversions(unittest.TestCase):
    """US1: Pruebas de conversión entre escalas distintas y referencias verificables."""

    def test_celsius_to_fahrenheit(self):
        # 0 C -> 32.00 F
        res = convertir_temperatura(0.0, "C", "F")
        self.assertAlmostEqual(res, 32.0, places=2)
        self.assertEqual(formatear_resultado(res, "F"), "32.00 F")

        # 100 C -> 212.00 F
        res_100 = convertir_temperatura(100.0, "C", "F")
        self.assertAlmostEqual(res_100, 212.0, places=2)
        self.assertEqual(formatear_resultado(res_100, "F"), "212.00 F")

        # -40 C -> -40.00 F
        res_40 = convertir_temperatura(-40.0, "C", "F")
        self.assertAlmostEqual(res_40, -40.0, places=2)
        self.assertEqual(formatear_resultado(res_40, "F"), "-40.00 F")

    def test_fahrenheit_to_celsius(self):
        # 32 F -> 0.00 C
        res = convertir_temperatura(32.0, "F", "C")
        self.assertAlmostEqual(res, 0.0, places=2)
        self.assertEqual(formatear_resultado(res, "C"), "0.00 C")

        # 212 F -> 100.00 C
        res_212 = convertir_temperatura(212.0, "F", "C")
        self.assertAlmostEqual(res_212, 100.0, places=2)
        self.assertEqual(formatear_resultado(res_212, "C"), "100.00 C")

        # -40 F -> -40.00 C
        res_40 = convertir_temperatura(-40.0, "F", "C")
        self.assertAlmostEqual(res_40, -40.0, places=2)
        self.assertEqual(formatear_resultado(res_40, "C"), "-40.00 C")

    def test_celsius_to_kelvin(self):
        # 0 C -> 273.15 K
        res = convertir_temperatura(0.0, "C", "K")
        self.assertAlmostEqual(res, 273.15, places=2)
        self.assertEqual(formatear_resultado(res, "K"), "273.15 K")

    def test_kelvin_to_celsius(self):
        # 273.15 K -> 0.00 C
        res = convertir_temperatura(273.15, "K", "C")
        self.assertAlmostEqual(res, 0.0, places=2)
        self.assertEqual(formatear_resultado(res, "C"), "0.00 C")

    def test_fahrenheit_to_kelvin_combinado(self):
        # 32 F -> 273.15 K (sin redondeo intermedio)
        res = convertir_temperatura(32.0, "F", "K")
        self.assertAlmostEqual(res, 273.15, places=2)
        self.assertEqual(formatear_resultado(res, "K"), "273.15 K")

    def test_kelvin_to_fahrenheit_combinado(self):
        # 273.15 K -> 32.00 F (sin redondeo intermedio)
        res = convertir_temperatura(273.15, "K", "F")
        self.assertAlmostEqual(res, 32.0, places=2)
        self.assertEqual(formatear_resultado(res, "F"), "32.00 F")

    def test_formateo_cero_negativo(self):
        # Evitar "-0.00"
        self.assertEqual(formatear_resultado(-0.000000001, "C"), "0.00 C")


class TestUserStory2SameUnit(unittest.TestCase):
    """US2: Conversión con misma unidad de origen y destino."""

    def test_misma_unidad_celsius(self):
        res = convertir_temperatura(25.0, "C", "C")
        self.assertEqual(res, 25.0)
        self.assertEqual(formatear_resultado(res, "C"), "25.00 C")

        # Límite cero absoluto en misma unidad
        res_lim = convertir_temperatura(-273.15, "C", "C")
        self.assertEqual(res_lim, -273.15)
        self.assertEqual(formatear_resultado(res_lim, "C"), "-273.15 C")

    def test_misma_unidad_fahrenheit(self):
        res = convertir_temperatura(68.5, "F", "F")
        self.assertEqual(res, 68.5)
        self.assertEqual(formatear_resultado(res, "F"), "68.50 F")

    def test_misma_unidad_kelvin(self):
        res = convertir_temperatura(300.0, "K", "K")
        self.assertEqual(res, 300.0)
        self.assertEqual(formatear_resultado(res, "K"), "300.00 K")


class TestUserStory3AbsoluteZero(unittest.TestCase):
    """US3: Validación de límites físicos y cero absoluto."""

    def test_rechazo_inferior_cero_absoluto_celsius(self):
        valido, err = validar_cero_absoluto(-273.16, "C")
        self.assertFalse(valido)
        self.assertEqual(err, "Temperatura inferior al cero absoluto")

    def test_rechazo_inferior_cero_absoluto_fahrenheit(self):
        valido, err = validar_cero_absoluto(-459.68, "F")
        self.assertFalse(valido)
        self.assertEqual(err, "Temperatura inferior al cero absoluto")

    def test_rechazo_inferior_cero_absoluto_kelvin(self):
        valido, err = validar_cero_absoluto(-0.01, "K")
        self.assertFalse(valido)
        self.assertEqual(err, "Temperatura inferior al cero absoluto")

    def test_aceptacion_limites_exactos(self):
        # -273.15 C es válido
        valido_c, err_c = validar_cero_absoluto(-273.15, "C")
        self.assertTrue(valido_c)
        self.assertIsNone(err_c)
        res_k = convertir_temperatura(-273.15, "C", "K")
        self.assertEqual(formatear_resultado(res_k, "K"), "0.00 K")

        # -459.67 F es válido
        valido_f, err_f = validar_cero_absoluto(-459.67, "F")
        self.assertTrue(valido_f)
        self.assertIsNone(err_f)
        res_c = convertir_temperatura(-459.67, "F", "C")
        self.assertEqual(formatear_resultado(res_c, "C"), "-273.15 C")

        # 0 K es válido
        valido_k, err_k = validar_cero_absoluto(0.0, "K")
        self.assertTrue(valido_k)
        self.assertIsNone(err_k)
        res_ck = convertir_temperatura(0.0, "K", "C")
        self.assertEqual(formatear_resultado(res_ck, "C"), "-273.15 C")


if __name__ == "__main__":
    unittest.main()
