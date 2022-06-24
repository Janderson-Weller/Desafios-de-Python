def menu():
    switch = {
        1: "Reproduzir",
        2: "Parar",
        3: "Pesquisar",
        4: "Adicionar Música",
        5: "Sair"
    }

    for i in switch:
        print("[", i, "]", switch[i])

    opcao = int(input("Digite sua opção: "))
    op = switch.get(opcao)

    if opcao < len(switch):
        print("Você selecionou a opção", op)

    return opcao


