#Especificações
print('*****************************')
print('*****************************')
print('    HOTEL DOS ANIMAIS')
print('*****************************')
print('*****************************')
print('Especificando posições:')
print('[1,2,3,4,]')
print('[5,6,7,8,]')
print('OBS: As posições com "*" já estão alocadas, escolha uma casa vazia "_"')
print(
)
print('Regras do jogo:')
print('• O rato não pode ficar ao lado do gato')
print('• O cão não pode ficar ao lado do osso')
print('• O gato não pode ficar ao lado do cão')
print('• O queijo não pode ficar ao lado do rato')
print(
)
print('Especificando das Letras:')
print('G – GATO')
print('C – CÃO')
print('R – RATO')
print('O – OSSO')
print('Q – QUEIJO')
print(
)

#*******************************************


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
def matrizF1():
    linha1[2] = '_'
    linha1[3] = 'G'
    linha2[0] = 'R'
    linha2[1] = '_'
    matrizF1a = (linha1)
    matrizF1b = (linha2)
    print(matrizF1a)
    print(matrizF1b)
def matrizF2():
    linha1[0] = '_'
    linha2[1] = 'C'
    linha2[2] = '_'
    linha2[3] = '_'
    matrizF2a = (linha1)
    matrizF2b = (linha2)
    print(matrizF2a)
    print(matrizF2b)
def matrizF3():
    linha1[0] = '_'
    linha2[0] = '_'
    linha2[1] = 'G'
    linha2[2] = '*'
    matrizF3a = (linha1)
    matrizF3b = (linha2)
    print(matrizF3a)
    print(matrizF3b)

linha1 = ['*', '*', '*', '*']
linha2 = ['*', '*', '*', '*']
fase = 1
continuar = 1

# programa principal
def primeiraFase():
    while True:
        print('Bem vindo a faze 1!')
        print('Na fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que representa  os quartos:')
        matrizF1()
        rato = int(input(print('Em qual posição você quer alocar o RATO? ')))
        while (rato != 3 and rato != 6):
            print('Quarto indisponível!')
            rato = int(input(print('Em qual posição você quer alocar o RATO? ')))
        gato = int(input(print('Em qual posição você quer alocar o GATO? ')))
        while (gato != 3 and gato != 6 or gato == rato):
            print('Quarto indisponível!')
            gato = int(input(print('Em qual posição você quer alocar o GATO? ')))
        if (rato == 3 and gato == 6):
            print('Game Over!!!')
            print('Você perdeu... ')
            continuar = int(input(print('Deseja jogar novamente? 1 - SIM  0 - NÃO')))
            if (continuar == 0):
                break
            else:
                separaFase()
        elif (rato == 6 and gato == 3):
            borda('Parabéns. Passou de fase!!!')
            fase = 2
            segundaFase()
def segundaFase():
    while True:
        separaFase()
        print('Bem vindo a faze 2!')
        print('Na segunda fase o jogador deve alocar : CÃO, CÃO E OSSO')
        matrizF2()
        caoA= int(input(print('Em qual posição você quer alocar o primeiro CÃO? ')))
        while (caoA != 1 and caoA != 7 and caoA != 8):
            print('Quarto indisponível!')
            caoA = int(input(print('Em qual posição você quer alocar o primeiro CÃO? ')))
        caoB= int(input(print('Em qual posição você quer alocar o segundo CÃO? ')))
        while (caoB != 1 and caoB != 7 and caoB != 8 or caoA==caoB):
            print('Quarto indisponível!')
            caoB = int(input(print('Em qual posição você quer alocar o segundo CÃO? ')))
        osso= int(input(print('Em qual posição você quer alocar o OSSO? ')))
        while (osso != 1 and osso != 7 and osso != 8 or osso==caoB or osso==caoA):
            print('Quarto indisponível!')
            osso= int(input(print('Em qual posição você quer alocar o OSSO? ')))
        if(osso!=1):
            print('Game Over!!!')
            print('Você perdeu...')
            break
        else:
            borda('Parabéns. Passou de fase!!!')
            separaFase()
            terceiraFase()
def terceiraFase():
    while True:
        print('Bem vindo a faze 3!')
        print('Na fase 3 o jogador deverá alocar : GATO, RATO E OSSO.')
        matrizF3()
        gato = int(input(print('Em qual posição você quer alocar o GATO? ')))
        while (gato != 1 and gato != 5 and gato != 7):
            print('Quarto indisponível!')
            gato = int(input(print('Em qual posição você quer alocar o GATO? ')))
        rato = int(input(print('Em qual posição você quer alocar o RATO? ')))
        while (rato != 1 and rato != 5 and rato != 7 or gato == rato):
            print('Quarto indisponível!')
            rato = int(input(print('Em qual posição você quer alocar o RATO? ')))
        osso = int(input(print('Em qual posição você quer alocar o OSSO? ')))
        while (osso != 1 and osso != 5 and osso != 7 or osso == rato or osso == gato):
            print('Quarto indisponível!')
            osso = int(input(print('Em qual posição você quer alocar o OSSO? ')))
        if (rato != 1 and osso != 5 and gato != 7):
            print('Game Over!!!')
            print('Você perdeu... ')
            continuar = int(input(print('Deseja jogar novamente? 1 - SIM  0 - NÃO')))
            if (continuar == 0):
                break
            else:
                separaFase()
        elif (rato == 1 and osso == 5 and gato == 7):
            borda('Parabéns. Passou de fase!!!')
            break





# programa principal:

primeiraFase()


