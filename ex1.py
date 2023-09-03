import os
from time import sleep

# Inicializa o tabuleiro 4x4 preenchido com 0
tabuleiro = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


def imprime_tabuleiro():
    """
    Imprime o tabuleiro atualizado com o símbolo de cada jogador.

    'X' é representado na cor vermelha e 'O' é representado na cor azul.
    As casas vazias são representadas por '0'.
    """
    for casa in tabuleiro:
        lista_formatada = ' | '.join(
            [f'\033[91mX\033[0m' if c == 'X' else f'\033[94mO\033[0m' if c == 'O' else str(c) for c in casa])
        print(lista_formatada)
        print("--+---+---+---")


def ganhou():
    """
    Verifica se um jogador ganhou o jogo.
    Ele retorna verdadeiro caso um dos jogadores ganhe a partida, caso contrário ele retorna Falso.
    """

    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] == linha[3] != 0:
            return True
    for coluna in range(4):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == tabuleiro[3][coluna] != 0:
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == tabuleiro[3][3] != 0:
        return True

    if tabuleiro[0][3] == tabuleiro[1][2] == tabuleiro[2][1] == tabuleiro[3][0] != 0:
        return True
    return False


def empate():
    """
    Verifica se o jogo terminou em empate.
    Ele retorna verdadeiro caso o jogo tenha um empate, caso contrário ele retorna Falso.
    """

    for linha in tabuleiro:
        if 0 in linha:
            return False
    return True


def limpar_tela():
    """
    Limpa a tela do console
    """
    os.system('cls')


def jogar():
    """
    Função main do jogo da velha.

    Essa função inicia o jogo, faz o gerenciamento das jogadas dos jogadores,
    verifica se há um vencedor ou empate e imprime o resultado final.
    """

    # Inicializa as variáveis do jogo
    jogada = 0
    jogador1 = 'X'
    jogador2 = 'O'

    while True:

        print(f"jogador {jogada%2 + 1}")
        imprime_tabuleiro()
        try:
            linha = int(input("Digite a linha: "))
            coluna = int(input("Digite a coluna: "))
            if linha < 1 or linha > 4 or coluna < 1 or coluna > 4:
                print("Coordenada digitada está fora do limite do tabuleiro.")
                sleep(2)
                limpar_tela()
                continue
        except ValueError:
            print("Valor inválido\n")
            sleep(1)
        else:

            try:
                if tabuleiro[linha-1][coluna-1] == 0:
                    if (jogada % 2+1) == 1:
                        tabuleiro[linha-1][coluna-1] = jogador1
                    else:
                        tabuleiro[linha-1][coluna-1] = jogador2
                else:
                    print("Casa já está ocupada")
                    sleep(1)
                    jogada -= 1
                jogada += 1

            except IndexError:
                print("Valor inválido")
            else:

                if ganhou():
                    limpar_tela()
                    imprime_tabuleiro()
                    print(f"{'[ O ]' if jogada%2+1 == 1 else '[ X ]'} ganhou")
                    # Caso rode no terminal, ele mantem a tela por 5 segundos antes de fechar o mesmo
                    sleep(5)
                    break
                elif empate():
                    limpar_tela()
                    imprime_tabuleiro()
                    print("Deu velha")
                    sleep(5)
                    break
        limpar_tela()


if __name__ == '__main__':
    jogar()
