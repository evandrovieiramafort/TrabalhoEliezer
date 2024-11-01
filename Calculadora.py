class Calculadora:
    def __init__(self, numero1=0, numero2=0):
        self.numero1 = numero1
        self.numero2 = numero2

    @property
    def numero1(self):
        return self._numero1

    @numero1.setter
    def numero1(self, numero1):
        self._numero1 = numero1

    @property
    def numero2(self):
        return self._numero2

    @numero2.setter
    def numero2(self, numero2):
        self._numero2 = numero2

    def soma(self):
        return self.numero1 + self.numero2

    def subtracao(self):
        return self.numero1 - self.numero2

    def multiplicacao(self):
        return self.numero1 * self.numero2

    def divisao(self):
        if self.numero2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return self.numero1 / self.numero2
