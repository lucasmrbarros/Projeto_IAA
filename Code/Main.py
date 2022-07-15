import funcoes

jogo = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

sair = 0
iteracao = 0

while sair == 0:

    print()

    if iteracao == 9:
        sair = 1
    else:
        funcoes.print_jogo(jogo)
        print()
        print("Selecione uma das casas disponíeis: ")

        jogada_usuario = int(input())
        funcoes.jogada_humano(jogada_usuario, jogo)

        decisao = int(input())
        funcoes.jogada_maquina(decisao, jogo)

        iteracao + 1
