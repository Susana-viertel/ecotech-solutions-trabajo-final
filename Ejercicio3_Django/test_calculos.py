import unittest

from calculos import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):

    # Prueba 1: calcular emisiones correctamente
    def test_calculo_emisiones_correcto(self):
        resultado = calcular_emisiones_carbono(100)
        self.assertEqual(resultado, 40.0)

    # Prueba 2: comprobar consumo cero
    def test_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0)
        self.assertEqual(resultado, 0.0)

    # Prueba 3: comprobar consumo negativo
    def test_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)


if __name__ == "__main__":
    unittest.main()