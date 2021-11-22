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

def matrizF3():
    linha1[0] = '_'
    linha2[0] = '_'
    linha2[1] = 'G'
    linha2[2] = '_'
    matrizF3a = (linha1)
    matrizF3b = (linha2)
    print(matrizF3a)
    print(matrizF3b)




while True:
    print('Bem vindo a faze 3!')
    print('Na fase 3 o jogador deverá alocar : GATO, RATO E OSSO.')
    matrizF3()
    gato= int(input(print('Em qual posição você que alocar o GATO? ')))
    while (gato != 1 and gato != 5 and gato != 7):
            print('Quarto indisponível!')
            gato= int(input(print('Em qual posição você que alocar o GATO? ')))
    rato= int(input(print('Em qual posição você que alocar o RATO? ')))
    while (rato != 1 and rato != 5 and rato != 7 or gato==rato):
            print('Quarto indisponível!')
            rato = int(input(print('Em qual posição você que alocar o RATO? ')))
    osso= int(input(print('Em qual posição você que alocar o OSSO? ')))
    while (osso != 1 and osso != 5 and osso != 7 or osso==rato or osso==gato):
            print('Quarto indisponível!')
            osso= int(input(print('Em qual posição você que alocar o OSSO? ')))
    if(rato != 1 and osso!= 5 and gato!= 7):
        print('Game Over!!!')
        print('Você perdeu... ')
        continuar = int(input(print('Deseja jogar novamente? 1 - SIM  0 - NÃO')))
        if (continuar == 0):
            break
        else:
            separaFase()
    elif (rato == 1 and osso == 5 and gato==7):
        borda('Parabéns. Você Ganhou!!!')
        break





