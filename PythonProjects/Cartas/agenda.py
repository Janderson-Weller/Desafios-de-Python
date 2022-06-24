class Contatos:
    def __init__(self, nome, numero):
        self._nome = nome
        self._numero = numero

    def mostraDados(self):
        return f'Nome: {self._nome} Número: {self._numero}'

class Agenda:
    contato = []

    def adiciona(self, object):
        self.contato.append(object)


c1 = Contatos("Fulano de tal", 1234)
c2 = Contatos("Nada a Ver", 45678)

a = Agenda()
a.adiciona(c1.mostraDados())
a.adiciona(c2.mostraDados())

print(a.contato)