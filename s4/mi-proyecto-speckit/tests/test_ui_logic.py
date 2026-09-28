"""Pruebas unitarias para la lógica de validación de entrada y controlador de interfaz."""

import unittest
from conversor.core import (
    procesar_conversion,
    validar_entrada_temperatura,
)


class TestUserStory4InputValidation(unittest.TestCase):
    """US4: Validación y manejo de datos de entrada no válidos."""

    def test_entrada_vacia_o_solo_espacios(self):
        val, err = validar_entrada_temperatura(None)
        self.assertIsNone(val)
        self.assertEqual(err, "Ingrese una temperatura")

        val, err = validar_entrada_temperatura("")
        self.assertIsNone(val)
        self.assertEqual(err, "Ingrese una temperatura")

        val, err = validar_entrada_temperatura("   \t \n  ")
        self.assertIsNone(val)
        self.assertEqual(err, "Ingrese una temperatura")

        # A través de procesar_conversion
        ok, msg = procesar_conversion("", "C", "F")
        self.assertFalse(ok)
        self.assertEqual(msg, "Ingrese una temperatura")

        ok, msg = procesar_conversion("   ", "C", "F")
        self.assertFalse(ok)
        self.assertEqual(msg, "Ingrese una temperatura")

    def test_entrada_no_numerica(self):
        val, err = validar_entrada_temperatura("abc")
        self.assertIsNone(val)
        self.assertEqual(err, "Ingrese un número válido")

        val, err = validar_entrada_temperatura("12.34.56")
        self.assertIsNone(val)
        self.assertEqual(err, "Ingrese un número válido")

        val, err = validar_entrada_temperatura("100F")
        self.assertIsNone(val)
        self.assertEqual(err, "Ingrese un número válido")

        # A través de procesar_conversion
        ok, msg = procesar_conversion("abc", "C", "F")
        self.assertFalse(ok)
        self.assertEqual(msg, "Ingrese un número válido")

    def test_entrada_numerica_valida(self):
        val, err = validar_entrada_temperatura("25")
        self.assertEqual(val, 25.0)
        self.assertIsNone(err)

        # Con espacios alrededor
        val, err = validar_entrada_temperatura("   -40.5   ")
        self.assertEqual(val, -40.5)
        self.assertIsNone(err)

        # Con coma decimal
        val, err = validar_entrada_temperatura("25,5")
        self.assertEqual(val, 25.5)
        self.assertIsNone(err)


class TestUserStory5ConsecutiveConversions(unittest.TestCase):
    """US5: Conversiones sucesivas independientes sin persistencia de estados previos."""

    def test_recuperacion_tras_error(self):
        # 1. Operación exitosa
        ok1, res1 = procesar_conversion("100", "C", "F")
        self.assertTrue(ok1)
        self.assertEqual(res1, "212.00 F")

        # 2. Entrada inválida inmediatamente después (no debe conservar res1)
        ok2, err2 = procesar_conversion("abc", "C", "F")
        self.assertFalse(ok2)
        self.assertEqual(err2, "Ingrese un número válido")
        self.assertNotEqual(err2, res1)

        # 3. Nueva operación válida tras el error
        ok3, res3 = procesar_conversion("0", "C", "K")
        self.assertTrue(ok3)
        self.assertEqual(res3, "273.15 K")

    def test_recuperacion_tras_cero_absoluto(self):
        # 1. Intento por debajo del cero absoluto
        ok1, err1 = procesar_conversion("-300", "C", "F")
        self.assertFalse(ok1)
        self.assertEqual(err1, "Temperatura inferior al cero absoluto")

        # 2. Inmediatamente corregido a valor válido
        ok2, res2 = procesar_conversion("-273.15", "C", "K")
        self.assertTrue(ok2)
        self.assertEqual(res2, "0.00 K")


if __name__ == "__main__":
    unittest.main()
