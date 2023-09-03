import rich
from rich.console import Console
from rich.prompt import Prompt
import random

MAX_TENTATIVAS = 6

teclado = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']
]

teclas_usadas = []
letras_lugar_certo = []
letras_certas = []
letras_palavra = []


def imprime_teclado(teclado, teclas_usadas, letras_lugar_certo, letras_certas):
    """
    Imprime o layout do teclado, formatado com letras coloridas, apresentando se a letra está certa e no lugar correto,
    letra certa mas no lugar errado ou se a letra não está presente na palavra
    """
    print('')
    for linha in teclado:
        teclado_formatado = []
        for tecla in linha:
            if tecla in teclas_usadas:
                if tecla in letras_lugar_certo:
                    teclado_formatado.append(
                        f'\033[42;1;42m{[tecla]}\033[0;0m')
                elif tecla in letras_certas:
                    teclado_formatado.append(
                        f'\033[42;1;43m{[tecla]}\033[0;0m')
                else:
                    teclado_formatado.append(
                        f'\033[42;1;40m{[tecla]}\033[0;0m')

            else:

                teclado_formatado.append(f'\033[42;1;47m{[tecla]}\033[0;0m')
        print(' '.join(teclado_formatado))


def remove_letras_usadas(palavra):
    """
    Adiciona as letras das palavras usadas para a lista de teclas usadas
    """
    for letra in palavra:
        if letra not in teclas_usadas:
            teclas_usadas.append(letra)


def escolhe_palavra():
    """
    Escolhe uma palavra aleatória do arquivo "lista_palavras.txt", baseado no critério especificado do tamanho da palavra
    """
    arquivo = open(
        "X:\VSCode\Yann\Python ListaExercícios1\lista_palavras.txt", "r", encoding="UTF-8")
    palavras = []
    for linha in arquivo:
        linha = linha.strip().lower()
        palavras.append(linha)
    arquivo.close()
    palavra_secreta = numero_letras(palavras)

    # print(palavra_secreta) para fins de testes, essa linha imprime a palavra_secreta para verificação do programador
    return palavra_secreta


def numero_letras(palavras):
    """
    Filtra as palavras de acordo com o tamanho especificado pelo usuario.
    Caso ele não encontre uma palavra com o tamanho especificado, ele escolhe uma palavra aleatoria de qualquer tamanho
    """
    num_letras = int(input("Digite o número de letras da palavra secreta: "))
    palavra_x_letras = []
    [palavra_x_letras.append(x) for x in palavras if int(len(x)) == num_letras]
    if (len(palavra_x_letras) == 0):
        print("Não existe palavras com a quantidade de caracteres especificados, escolhendo uma palavra aleatória...")
        palavra_secreta = random.choice(palavras)
        return palavra_secreta
    else:
        print("Escolhendo uma palavra...")
        palavra = random.choice(palavra_x_letras)
        return palavra


emojis = {
    'lugar_certo': '🟩',
    'letra_certa': '🟨',
    'errado': '⬜'
}


def lugar_certo(letra):
    """
    Armazena a letra em letras_lugar_certo
    """
    letras_lugar_certo.append(letra)
    return f'[black on green]{letra}[/]'


def letra_certa(letra):
    """
    Armazena a letra em letras_certas
    """
    letras_certas.append(letra)
    return f'[black on yellow]{letra}[/]'


def errado(letra):
    """
    Armazena a letra em teclas_usadas
    """
    teclas_usadas.append(letra)
    return f'[black on white]{letra}[/]'


def pontos_chute(chute, palavra):
    """
    Calcula e formata os pontos e os emojies baseado no chute do jogador
    """
    pontos = []
    emoji = []
    for i, letra in enumerate(chute):
        if palavra[i] == chute[i]:
            pontos += lugar_certo(letra)
            emoji.append(emojis['lugar_certo'])
        elif letra in palavra:
            pontos += letra_certa(letra)
            emoji.append(emojis['letra_certa'])
        else:
            pontos += errado(letra)
            emoji.append(emojis['errado'])
    return ''.join(pontos), ''.join(emoji)


def recebe_chute():
    """
    Recebe e processa o chute do jogador
    """
    chute = input("Digite uma palavra: ")
    chute = chute.strip().lower()
    return chute


def jogar():
    """
    Função principal do jogo para controlar o fluxo do jogo
    """
    console = Console()
    tentativas = 0
    palavra_secreta = escolhe_palavra()
    emojies = []
    todos_pontos = []
    while tentativas <= MAX_TENTATIVAS:
        tentativas += 1
        chute = recebe_chute()
        if len(chute) != len(palavra_secreta):
            print(
                f"Apenas palavras com {len(palavra_secreta)} letras são válidas")
            tentativas -= 1
            continue
        remove_letras_usadas(chute)
        pontos, emoji = pontos_chute(chute, palavra_secreta)
        todos_pontos.append(pontos)
        emojies.append(emoji)
        for pontos in todos_pontos:
            console.print(pontos)

        imprime_teclado(teclado, teclas_usadas,
                        letras_lugar_certo, letras_certas)

        if chute == palavra_secreta:
            print("Parabéns!! Você ganhou")
            break
    for em in emojies:
        print(em)
    print(f"A palavra secreta era: {palavra_secreta}")


if __name__ == '__main__':
    jogar()
