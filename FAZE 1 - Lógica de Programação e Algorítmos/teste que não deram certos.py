from random import randint  # IMPORTAR FUNÇÃO QUE GERA NUMERO ALEATÓRIO

listaInscricoes = []  # variável/lista (global) criada para que o dicionario não se perca


# FUNÇÕES
def menuPrincipal():
    print('\n-------------------Menu---------------------\n')
    try:
        opcao = int(input(print('1 - Nova inscrição\n2 - Visualizar inscrição\n0 -
        Encerrar\nOpção
        escolhida: '))) #lista de opções do menu principal
        if -1 < opcao < 3:  # aceitar somente numeros de 0 à 2
            return opcao
    else:  # caso não seja uma opção válida
    print('\nErro: digite uma opção válida!')
    menuPrincipal()
    except ValueError:
    print('\nErro: digite uma opção válida!')
    menuPrincipal()


def novaInscricao():
    voucher = randint(100, 400)  # para gerar numero aleatório
    nome = input('Digite seu nome: ')
    email = input('Digite e-mail: ')
    telefone = int(input('Digite telefone: '))
    curso = input('Digite curso: ')
    dicionarioInscricao = {'voucher': voucher, 'nome': nome, 'email': email,
                           'telefone': telefone, 'curso': curso}
    listaInscricoes.append(dicionarioInscricao)  # dicionario salvo na lista de inscrições


def visualizarInscricao():
    print('\n--------------Lista inscritos--------------\n')
    if len(listaInscricoes) == 0:  # se a lista estiver vazia, faça o print abaixo:
        print('Nenhuma inscrição cadastrada')
    else:  # para lista com conteúdo, exibir o mesmo na tela
        for inscricoes in listaInscricoes:
            for key, value in inscricoes.items():
                print('{} : {}'.format(key, value))
    print('\n')  # Separar inscrições


# PROGRAMA PRINCIPAL
while True:
    opcaoMenu = menuPrincipal()
    if opcaoMenu == 1:
        novaInscricao()
    elif opcaoMenu == 2:
        visualizarInscricao()
    elif opcaoMenu == 0:
    break
