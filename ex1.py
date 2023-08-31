import os
from time import sleep

tabuleiro = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


def imprime_tabuleiro():
    for casa in tabuleiro:
        lista_formatada = ' | '.join(
            [f'\033[91mX\033[0m' if c == 'X' else f'\033[94mO\033[0m' if c == 'O' else str(c) for c in casa])
        # lista_formatada = ' | '.join(map(str, casa))
        print(lista_formatada)
        print("--+---+---+---")


def ganhou():
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
    for linha in tabuleiro:
        if 0 in linha:
            return False
    return True


def limpar_tela():
    os.system('cls')


jogada = 0
jogador1 = 'X'
jogador2 = 'O'

while True:
    limpar_tela()
    print(f"jogador {jogada%2 + 1}")
    imprime_tabuleiro()
    # jogador = input("Digite a coordenada da jogada[linha][coluna]: ")
    # linha, coluna = [int(posicao) for posicao in jogador.split()]
    try:
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        if linha < 1 or linha > 4 or coluna < 1 or coluna > 4:
            print("Coordenada digitada está fora do limite do tabuleiro.")
            continue
    except ValueError:
        print("Valor inválido\n")
    else:

        try:
            if tabuleiro[linha-1][coluna-1] == 0:
                if (jogada % 2+1) == 1:
                    tabuleiro[linha-1][coluna-1] = jogador1
                else:
                    tabuleiro[linha-1][coluna-1] = jogador2
            else:
                print("Casa já está ocupada")
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
