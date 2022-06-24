class Calculadora:
    def __init__(self, num1, num2):
        self.a = float(num1)
        self.b = float(num2)

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        if self.b != 0:
            return self.a / self.b
        else:
            print("Erro")