import unittest
from calculadora import sumar, restar, multiplicar, dividir


class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 3), 12)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)


if __name__ == "__main__":
    unittest.main()
