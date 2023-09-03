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
    for letra in palavra:
        if letra not in teclas_usadas:
            teclas_usadas.append(letra)


def escolhe_palavra():
    arquivo = open(
        "X:\VSCode\Yann\Python ListaExercícios1\words.txt", "r", encoding="UTF-8")
    palavras = []
    for linha in arquivo:
        linha = linha.strip().lower()
        palavras.append(linha)
    arquivo.close()
    palavra_secreta = random.choice(palavras)
    print(palavra_secreta)
    return palavra_secreta


def numero_letras(palavras):
    num_letras = int(input("Digite o número de letras da palavra secreta: "))
    palavra_x_letras = []
    [palavra_x_letras.append(x) for x in palavras if int(len(x)) == num_letras]
    if (len(palavra_x_letras) == 0):
        print("Não existe palavras com a quantidade de caracteres especificados, escolhendo uma palavra aleatória...")
        numero_palavra = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero_palavra].upper()
        return palavra_secreta
    else:
        print("Escolhendo uma palavra...")
        palavra = random.choice(palavra_x_letras)
        return palavra


emojis = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect': '⬜'
}


def correct_place(letter):
    letras_lugar_certo.append(letter)
    return f'[black on green]{letter}[/]'


def correct_letter(letter):
    letras_certas.append(letter)
    return f'[black on yellow]{letter}[/]'


def incorrect(letter):
    teclas_usadas.append(letter)
    return f'[black on white]{letter}[/]'


def score_guess(guess, answer):
    scored = []
    emojied = []
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            scored += correct_place(letter)
            emojied.append(emojis['correct_place'])
        elif letter in answer:
            scored += correct_letter(letter)
            emojied.append(emojis['correct_letter'])
        else:
            scored += incorrect(letter)
            emojied.append(emojis['incorrect'])
    return ''.join(scored), ''.join(emojied)


def recebe_chute():
    chute = input("Digite uma palavra: ")
    chute = chute.strip().lower()
    return chute


def jogar():
    console = Console()
    tentativas = 0
    palavra_secreta = escolhe_palavra()
    all_emojied = []
    all_scored = []
    while tentativas <= MAX_TENTATIVAS:
        tentativas += 1
        chute = recebe_chute()
        remove_letras_usadas(chute)
        scored, emojied = score_guess(chute, palavra_secreta)
        all_scored.append(scored)
        all_emojied.append(emojied)
        for scored in all_scored:
            console.print(scored)

        imprime_teclado(teclado, teclas_usadas,
                        letras_lugar_certo, letras_certas)

        if chute == palavra_secreta:
            print("Parabéns!! Você ganhou")
            break
    for em in all_emojied:
        print(em)
    print(f"A palavra secreta era: {palavra_secreta}")


if __name__ == '__main__':
    jogar()
