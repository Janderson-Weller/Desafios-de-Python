class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def falar(self): #método, cada função
        print("Esta falando demais")

    def printing(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade, "anos")
        print("altura:", self.altura)