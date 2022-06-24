from musica import Reprodutor
from menu import menu


def main():
    i = 0
    lista = []
    while i != 5:
        i = menu()

        if i == 1:  # nome, artista, album, duracao
            #m1 = Reprodutor("vida", "nelson", "trajetória", 2)
            #print("Reproduzindo", m1)
            Reprodutor.mostraPlayList()

        elif i == 2:
            print("Musica Parada")

        elif i == 3:  # chama a função de pesquisa
            print("Qual musica deseja pesquisar?")

        elif i == 4:
            print("Adicionar musicas a sua playlist")
            Reprodutor("Vida", "Lisca", "Cantando a toa", 1.43).insereMusica()
            #lista.append(Reprodutor("OOOOI", "Ze Vaqueiro", "Vida um", 3.22))

        elif i == 5:
            print("Saindo...")

        else:
            print("Opção Inválida!")
            i = menu()
    # m1.insereMusica()
    # m2 = Reprodutor("tala", "iza", "nada", 3).insereMusica()
    # m3 = Reprodutor("life", "mattheus", "trajeto", 4)
    # lista_musica = [m1, m2]


if __name__ == '__main__':
    main()
