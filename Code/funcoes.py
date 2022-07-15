
##Funcao para print o jogo

def print_jogo(jogo):
    for i in range(3):
     print(jogo[i], end= "")

    print()

    for i in range(3, 6):
     print(jogo[i], end= "")

    print()

    for i in range(6, 9):
     print(jogo[i], end= "")

##Funcao que define a jogada do humano
def jogada_humano(casa, estado_jogo):
    estado_jogo[casa] = "O"
    return estado_jogo

##Funcao que define a jogada da maquina
def jogada_maquina(casa, estado_jogo):
    estado_jogo[casa] = "X"
    return estado_jogo