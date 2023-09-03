banco_usuarios = {}


def menu():
    """
    Menu principal do programa que apresenta as opções de cadastras ou imprimir usuários e a opção de sair do programa
    """
    print("\n+-------- MENU --------+")
    print("|[1] Cadastrar usuário |")
    print("|[2] Imprimir usuários |")
    print("|[0] Sair              |")
    print("+----------------------+")


def menu_imprimir_usuario():
    """
    Menu de impressão dos usuários, com direito a filtros como nome, campos e valores
    """
    print("\n+---------------- MENU ----------------+")
    print("|[1] Imprimir todos os usuários        |")
    print("|[2] Filtrar por nomes                 |")
    print("|[3] Filtrar por campos e valores      |")
    print("|[4] Filtrar por nomes e campos/valores|")
    print("|[5] Sair                              |")
    print("+--------------------------------------+")


campos_obrigatorios = []


def definir_campos_obrigatorios():
    """
    Permite que o usuário defina os campos obrigatórios para cadastrar usuários
    """

    global campos_obrigatorios

    # Pede para que o usuário insira o valor aos campos obrigatórios
    print("Definindo os campos obrigatórios\n")
    while True:
        campo_obrigatorio = input(
            "Digite um campo obrigatório (ou digite 'sair' para parar): ")
        if campo_obrigatorio.lower() == 'sair':
            break
        campos_obrigatorios.append(campo_obrigatorio)


def cadastrar_usuario(*campos_obrigatorios):
    """
    Possibilita cadastrar um novo usuário com os campos obrigatórios e com campos adicionais
    
    *campos_obrigatorios (Args): são os campos obrigatorios previamente definidos

    ele retorna um dicionario que representa o novo usuário que foi cadastrado
    """
    novo_usuario = {}
    for campo in campos_obrigatorios:
        novo_usuario[campo] = input(f"Digite o {campo} do usuário: ")

    while True:
        campo_adicional = input(
            "Digite um campo adicional (ou digite 'sair' para sair): ")
        if campo_adicional.lower() == 'sair':
            break
        valor_adicional = input(f"{campo_adicional}: ")
        novo_usuario[campo_adicional] = valor_adicional

    banco_usuarios[novo_usuario[campos_obrigatorios[0]]] = novo_usuario

    print("Usuário cadastrado com sucesso!")
    return novo_usuario


def imprimir_usuarios():
    """
    Possibilita imprimir as informações dos usuários com diversas opções de filtragem
    """
    menu_imprimir_usuario()
    op = int(input("Selecione uma das opções acima: "))

    usuarios_imprimir = []

    match op:
        case 1:
            usuarios_imprimir = banco_usuarios.values()
        case 2:
            nomes = input(
                "Digite os nomes separados por vírgula: ").split(", ")
            usuarios_imprimir = [
                user for user in banco_usuarios.values() if user["nome"] in nomes]
        case 3:
            campos = {}
            while True:
                campo = input(
                    "Digite o campo de busca (ou 'sair' para continuar): ")
                if campo.lower() == 'sair':
                    break
                valor = input(f"Digite o valor para o campo '{campo}': ")
                campos[campo] = valor
            for user in banco_usuarios.values():
                satisfaz_condicoes = all(
                    str(user.get(campo)) == valor for campo, valor in campos.items())
                if satisfaz_condicoes:
                    usuarios_imprimir.append(user)
        case 4:
            nomes = input(
                "Digite os nomes separados por vírgula: ").split(", ")
            campos = {}
            while True:
                campo = input(
                    "Digite o campo de busca (ou 'sair' para continuar): ")
                if campo.lower() == 'sair':
                    break
                valor = input(f"Digite o valor para o campo '{campo}': ")
                campos[campo] = valor
            for user in banco_usuarios.values():
                if user["nome"] in nomes:
                    satisfaz_condicoes = all(
                        str(user.get(campo)) == valor for campo, valor in campos.items())
                    if satisfaz_condicoes:
                        usuarios_imprimir.append(user)
        case 5:
            print("Saindo...")

        case _:
            print("Opção inválida...")

    print("Dados dos usuários:")
    for user in usuarios_imprimir:
        print(user)


def main():
    """
    Função principal para controlar todo o fluxo do programa
    """

    definir_campos_obrigatorios()
    cadastrar_usuario(*campos_obrigatorios)

    while True:
        menu()
        try:
            op = int(input("Selecione uma das opções acima: "))
        except ValueError:
            print("Valor digitado deve ser um número inteiro\n")
        else:
            match op:
                case 1:
                    cadastrar_usuario(*campos_obrigatorios)
                case 2:
                    imprimir_usuarios()
                case 0:
                    print("Encerrando o programa...")
                    break
                case _:
                    print("Opção inválida...")


if __name__ == '__main__':
    main()
