import pytest
from ops import MathOperations

@pytest.fixture
def math_ops():
    return MathOperations()

def test_add(math_ops):
    assert math_ops.add(3, 7) == 10

def test_subtract(math_ops):
    assert math_ops.subtract(10, 3) == 7

def test_multiply(math_ops):
    assert math_ops.multiply(4, 5) == 20

def test_divide(math_ops):
    assert math_ops.divide(10, 2) == 5
    with pytest.raises(ValueError, match="Erro: Divisão por zero não é permitida!"):
        math_ops.divide(10, 0)

def test_power(math_ops):
    assert math_ops.power(2, 3) == 8

def test_sqrt(math_ops):
    assert math_ops.sqrt(25) == 5
    with pytest.raises(ValueError, match="Erro: Não é possível calcular a raiz quadrada de um número negativo!"):
        math_ops.sqrt(-9)

def test_factorial(math_ops):
    assert math_ops.factorial(5) == 120
    assert math_ops.factorial(0) == 1
    with pytest.raises(ValueError, match="Erro: Fatorial de números negativos não é definido!"):
        math_ops.factorial(-1)

def test_calculate_expression(math_ops):
    assert math_ops.calculate_expression("2 + 3 * (4 - 1)") == 11
    assert math_ops.calculate_expression("10 / 2 + 6") == 11
    with pytest.raises(ValueError, match="Erro ao avaliar a expressão:"):
        math_ops.calculate_expression("10 / (2 - 2)")

def test_is_prime(math_ops):
    assert math_ops.is_prime(2) is True
    assert math_ops.is_prime(3) is True
    assert math_ops.is_prime(4) is False
    assert math_ops.is_prime(29) is True
    assert math_ops.is_prime(1) is False
    assert math_ops.is_prime(0) is False
    assert math_ops.is_prime(-5) is False
