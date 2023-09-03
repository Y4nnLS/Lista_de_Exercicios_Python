banco_usuarios = {}

def menu():
    print("+-------- MENU --------+")
    print("|[1] Cadastrar usuário |")
    print("|[2] Imprimir usuários |")
    print("|[0] Sair              |")
    print("+----------------------+")

def menu_imprimir_usuario():
    print("+---------------- MENU ----------------+")
    print("|[1] Imprimir todos os usuários        |")
    print("|[2] Filtrar por nomes                 |")
    print("|[3] Filtrar por campos e valores      |")
    print("|[4] Filtrar por nomes e campos/valores|")
    print("|[5] Sair                              |")
    print("+--------------------------------------+")

campos_obrigatorios = ('nome', 'sexo', 'idade')

def cadastrar_usuario(campos_obrigatorios):
    novo_usuario = {}
    for campo in campos_obrigatorios:
        novo_usuario[campo] = input(f"Digite o {campo} do usuário: ")
    banco_usuarios[novo_usuario[campos_obrigatorios[0]]] = novo_usuario
    print("Usuário cadastrado com sucesso!")
    return novo_usuario

def imprimir_usuarios():
    menu_imprimir_usuario()
    op = int(input("Selecione uma das opções acima: "))

    usuarios_imprimir = []

    match op:
        case 1:
            usuarios_imprimir = banco_usuarios.values()
        case 2:
            nomes = input("Digite os nomes separados por vírgula: ").split(", ")
            usuarios_imprimir = [user for user in banco_usuarios.values() if user["nome"] in nomes]
        case 3:
            campos = {}
            while True:
                campo = input("Digite o campo de busca (ou 'sair' para continuar): ")
                if campo.lower() == 'sair':
                    break
                valor = input(f"Digite o valor para o campo '{campo}': ")
                campos[campo] = valor
            for user in banco_usuarios.values():
                satisfies_conditions = all(str(user.get(campo)) == valor for campo, valor in campos.items())
                if satisfies_conditions:
                    usuarios_imprimir.append(user)
        case 4:
            nomes = input("Digite os nomes separados por vírgula: ").split(", ")
            campos = {}
            while True:
                campo = input("Digite o campo de busca (ou 'sair' para continuar): ")
                if campo.lower() == 'sair':
                    break
                valor = input(f"Digite o valor para o campo '{campo}': ")
                campos[campo] = valor
            for user in banco_usuarios.values():
                if user["nome"] in nomes:
                    satisfies_conditions = all(str(user.get(campo)) == valor for campo, valor in campos.items())
                    if satisfies_conditions:
                        usuarios_imprimir.append(user)
        case 5:
            print("Saindo...")
            return

        case _:
            print("Opção inválida...")
            return

    print("Dados dos usuários:")
    for user in usuarios_imprimir:
        print(user)

cadastrar_usuario(campos_obrigatorios)

while True:
    menu()
    try:
        op = int(input("Selecione uma das opções acima: "))
    except ValueError:
        print("Valor digitado deve ser um número inteiro\n")
    else:
        match op:
            case 1:
                cadastrar_usuario(campos_obrigatorios)
            case 2:
                imprimir_usuarios()
            case 0:
                print("Encerrando o programa...")
                break
            case _:
                print("Opção inválida...")
