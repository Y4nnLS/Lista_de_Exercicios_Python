import os
from time import sleep


def imprime_tabuleiro(tabuleiro):
    """
    Imprime o tabuleiro atualizado com o símbolo de cada jogador.
    'X' é representado na cor vermelha e 'O' é representado na cor azul.
    """

    for casa in tabuleiro:
        lista_formatada = ' | '.join(
            [f'\033[91mX\033[0m' if c == 'X' else f'\033[94mO\033[0m' if c == 'O' else str(c) for c in casa])
        print(lista_formatada)
        print("--+-" * (len(casa) - 1), end="--\n")


def limpar_tela():
    """
    Limpa a tela do console
    """
    os.system('cls')


def ganhou(tabuleiro, jogador, linha, coluna):
    """
    Verifica se um jogador ganhou o jogo.
    Ele retorna verdadeiro caso um dos jogadores ganhe a partida, caso contrário ele retorna Falso.
    """
    num_aux = len(tabuleiro)
    if all(tabuleiro[linha][c] == jogador for c in range(num_aux)):
        return True
    if all(tabuleiro[l][coluna] == jogador for l in range(num_aux)):
        return True
    if linha == coluna or linha + coluna == num_aux - 1:
        if all(tabuleiro[i][i] == jogador for i in range(num_aux)):
            return True
        if all(tabuleiro[i][num_aux - 1 - i] == jogador for i in range(num_aux)):
            return True
    return False


def empatou(tabuleiro):
    """
    Verifica se o jogo terminou em empate.
    Ele retorna verdadeiro caso o jogo tenha um empate, caso contrário ele retorna Falso.
    """
    return all(all(casa != ' ' for casa in linha) for linha in tabuleiro)


def main():
    """
    Função main do jogo da velha.

    Essa função inicia o jogo, solicita o tamanho do tabuleiro NxN, faz o gerenciamento das jogadas dos jogadores,
    verifica se há um vencedor ou empate e imprime o resultado final.
    """

    # Inicializa as variáveis do jogo
    n = int(input("Digite a dimensão do tabuleiro (NxN): "))
    tabuleiro = [[" " for _ in range(n)] for _ in range(n)]
    jogador = 'X'

    while True:
        try:
            imprime_tabuleiro(tabuleiro)
            print(f"Vez de jogador {jogador}")
            linha = int(input("Digite a linha: "))
            coluna = int(input("Digite a coluna: "))
            print(n)
            if linha < 1 or linha > n or coluna < 1 or coluna > n:
                print("Coordenada digitada está fora do limite do tabuleiro.")
                sleep(2)
                limpar_tela()
                continue
        except ValueError:
            print("Valor inválido\n")
            sleep(1)
        else:
            if tabuleiro[linha-1][coluna-1] == " ":
                tabuleiro[linha-1][coluna-1] = jogador

                if ganhou(tabuleiro, jogador, linha - 1, coluna - 1):
                    limpar_tela()
                    imprime_tabuleiro(tabuleiro)
                    print(f"[{jogador}] ganhou")
                    # Caso rode no terminal, ele mantem a tela por 5 segundos antes de fechar o mesmo
                    sleep(5)
                    break
                elif empatou(tabuleiro):
                    limpar_tela()
                    imprime_tabuleiro(tabuleiro)
                    print("Deu velha")
                    sleep(5)
                    break
                jogador = 'O' if jogador == 'X' else 'X'
            else:
                print("Casa já está ocupada")
                sleep(1)
        limpar_tela()


if __name__ == "__main__":
    main()
