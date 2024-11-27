import math

class MathOperations:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Erro: Divisão por zero não é permitida!")
        return x / y

    def power(self, x, y):
        return x ** y

    def sqrt(self, x):
        if x < 0:
            raise ValueError("Erro: Não é possível calcular a raiz quadrada de um número negativo!")
        return math.sqrt(x)

    def factorial(self, n):
        if n < 0:
            raise ValueError("Erro: Fatorial de números negativos não é definido!")
        return math.factorial(n)

    def calculate_expression(self, expression):
        """
        Avalia expressões matemáticas simples passadas como strings.
        Exemplo: "2 + 3 * (4 - 1)"
        """
        try:
            return eval(expression)
        except Exception as e:
            raise ValueError(f"Erro ao avaliar a expressão: {e}")

    def is_prime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
