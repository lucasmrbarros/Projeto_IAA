###interface jofo
branco = " "
token = ["X", "O"]


#gera o tabuleiro
def criarBoard():
    board = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco],
    ]
    return board

#exibe o tabuleiro
def printBoard(board):
    for i in range(3):
        print("|".join(board[i]))
        if (i < 2):
            print("------")

#Verifica se é uma jogada válida
def getInputValido(mensagem):
    try:
        n = int(input(mensagem))
        if (n >= 1 and n <= 3):
            return n - 1
        else:
            print("Numero precisa estar entra 1 e 3")
            return getInputValido(mensagem)
    except:
        print("Numero nao valido")
        return getInputValido(mensagem)


def verificaMovimento(board, i, j):
    if (board[i][j] == branco):
        return True
    else:
        return False

#Caso o movimento seja valido, adicona a matriz
def fazMovimento(board, i, j, jogador):
    board[i][j] = token[jogador]


#verificacoes de vencedor
def verificaGanhador(board):
    # linhas
    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != branco):
            return board[i][0]

    # coluna
    for i in range(3):
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != branco):
            return board[0][i]

    # diagonal principal
    if (board[0][0] != branco and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]

    # diagonal secundaria
    if (board[0][2] != branco and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]

    for i in range(3):
        for j in range(3):
            if (board[i][j] == branco):
                return False

    return "EMPATE"

#####################################################
######IA
#realiza a jogada da IA
def movimentoIA(board, jogador):
    possibilidades = getPosicoes(board)
    melhor_valor = None
    melhor_movimento = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = branco
        if (melhor_valor is None):
            melhor_valor = valor
            melhor_movimento = possibilidade
        elif (jogador == 0):
            if (valor > melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade
        elif (jogador == 1):
            if (valor < melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade

    return melhor_movimento[0], melhor_movimento[1]


#Define quais são as posições lvres.
def getPosicoes(board):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if (board[i][j] == branco):
                posicoes.append([i, j])

    return posicoes


score = {
    "EMPATE": 0,
    "X": 1,
    "O": -1
}

#Gera a arvore de possibilidades
def minimax(board, jogador):
    ganhador = verificaGanhador(board)
    if (ganhador):
        return score[ganhador]
    jogador = (jogador + 1) % 2

    possibilidades = getPosicoes(board)
    melhor_valor = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = branco

        if (melhor_valor is None):
            melhor_valor = valor
        elif (jogador == 0):
            if (valor > melhor_valor):
                melhor_valor = valor
        elif (jogador == 1):
            if (valor < melhor_valor):
                melhor_valor = valor

    return melhor_valor
