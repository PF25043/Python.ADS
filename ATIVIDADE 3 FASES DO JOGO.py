def separaFase():
    print('         |  |')
    print('         |  |')
    print('         |  |')
    print('         |  |')
    print('        \    /')
    print('         \  / ')
    print('          \/ ')
def borda(x):
    tam = len(x)
    if tam:
        print('+', '-' * tam, '+')
        print('|', x, '|')
        print('+', '-' * tam, '+')
linha1 = ['*', '*', '*', '*']
linha2 = ['*', '*', '*', '*']
fase = 1
continuar = 1

def matrizF4():
    linha1[0] = '_'
    linha1[1] = '_'
    linha1[2] = '_'
    linha2[1] = 'R'
    matrizF3a = (linha1)
    matrizF3b = (linha2)
    print(matrizF3a)
    print(matrizF3b)




while True:
    print('Bem vindo a faze 4!')
    print('Na fase 4, o jogador deverá alocar: QUEIJO, QUEIJO, OSSO.')
    matrizF4()
    queijoA= int(input(print('Em qual posição você quer alocar o primeiro QUEIJO? ')))
    while (queijoA != 1 and queijoA != 2 and queijoA != 3):
            print('Quarto indisponível!')
            queijo= int(input(print('Em qual posição você quer alocar o primeiro QUEIJO? ')))
    queijoB= int(input(print('Em qual posição você quer alocar o segundo QUEIJO? ')))
    while (queijoB != 1 and queijoB != 2 and queijoB != 3 or queijoB==queijoA):
            print('Quarto indisponível!')
            queijoB= int(input(print('Em qual posição você quer alocar o segundo QUEIJO? ')))
    osso= int(input(print('Em qual posição você quer alocar o OSSO? ')))
    while (osso != 1 and osso != 2 and osso != 3 or osso==queijoB or osso==queijoA):
            print('Quarto indisponível!')
            osso= int(input(print('Em qual posição você quer alocar o OSSO? ')))
    if( osso!= 2 ):
        print('Game Over!!!')
        print('Você perdeu... ')
        continuar = int(input(print('Deseja jogar novamente? 1 - SIM  0 - NÃO')))
        if (continuar == 0):
            break
        else:
            separaFase()
    else:
        borda('Parabéns. VocÊ Ganhou!!!')
        break





