class Musica:
    def __init__(self, nome, artista, album, duracao):
        self.nome = nome
        self.artista = artista
        self.album = album
        self.duracao = duracao

    def __str__(self):
        return f"nome: {self.nome} artista: {self.artista} album: {self.album} duração: {self.duracao}"

class Reprodutor(Musica):
    def __init__(self, nome, artista, album, duracao):
        super().__init__(nome, artista, album, duracao)
        self.lista_musica = []

    def insereMusica(self):
        self.lista_musica.append(object)

    def criaPlayList(self):
        if not self.lista_musica:
            self.insereMusica()
            print("PlayList Criada com Sucesso!")
        else:
            self.lista_musica.append(object)
            print("PlayList Atualizada")

    def mostraPlayList(self):
        if not self.lista_musica:
            print("Deseja adicionar músicas a sua playlist?")
           # self.criaPlayList()
        for n in self.lista_musica:
            #self.lista_musica.append(Musica)
            print(self.__str__())

    def Play(self):
        print("Exibindo Música")
        print("Musica: ", self.nome, "Autor: ", self.artista, "Album: ", self.album, "Duração: ", self.duracao)



#  def stopMusica(self):"""
