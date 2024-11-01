import unittest
from Calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()

    def test_soma(self):
        self.calculadora.numero1 = 2
        self.calculadora.numero2 = 3
        self.assertEqual(self.calculadora.soma(), 5)

    def test_subtracao(self):
        self.calculadora.numero1 = 5
        self.calculadora.numero2 = 2
        self.assertEqual(self.calculadora.subtracao(), 3)

    def test_multiplicacao(self):
        self.calculadora.numero1 = 3
        self.calculadora.numero2 = 4
        self.assertEqual(self.calculadora.multiplicacao(), 12)

    def test_divisao(self):
        self.calculadora.numero1 = 10
        self.calculadora.numero2 = 2
        self.assertEqual(self.calculadora.divisao(), 5)

    def test_divisao_por_zero(self):
        self.calculadora.numero1 = 10
        self.calculadora.numero2 = 0
        with self.assertRaises(ZeroDivisionError):
            self.calculadora.divisao()


if __name__ == '__main__':
    result = unittest.main(exit=False)
    if result.result.wasSuccessful():
        print("\nTodos os testes foram bem-sucedidos! ✅")
    else:
        print("\nAlguns testes falharam. ⚠️")
