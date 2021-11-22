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
    linha1 = ['*', '*', '_', 'G']
    linha2 = ['R', '_', '*', '*']
    matrizF1a = (linha1)
    matrizF1b = (linha2)
    print(matrizF1a)
    print(matrizF1b)
def matrizF2():
    linha1 = ['_', '*', '*', '*']
    linha2 = ['*', 'C', '_', '_']
    matrizF2a = (linha1)
    matrizF2b = (linha2)
    print(matrizF2a)
    print(matrizF2b)
def matrizF3():
    linha1 = ['_', '*', '*', '*']
    linha2 = ['_', 'G', '_', '*']
    matrizF3a = (linha1)
    matrizF3b = (linha2)
    print(matrizF3a)
    print(matrizF3b)
def matrizF4():
    linha1 = ['_', '_', '_', '*']
    linha2 = ['*', 'R', '*', '*']
    matrizF4a = (linha1)
    matrizF4b = (linha2)
    print(matrizF4a)
    print(matrizF4b)
def jogarNovamente():
    while True:
        cont = int(input(print('Deseja jogar novamente? 1 - SIM  0 - NÃO')))
        if (cont == 1):
            separaFase()
            primeiraFase()
        break

cont = 1

# função fazes
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
            jogarNovamente()
            break
        elif (rato == 6 and gato == 3):
            borda('Parabéns. Passou de fase!!!')
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
            jogarNovamente()
            break
        else:
            borda('Parabéns. Passou de fase!!!')
            separaFase()
            terceiraFase()
        break
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
        if (rato != 1 or osso != 5 or gato != 7):
            print('Game Over!!!')
            print('Você perdeu... ')
            jogarNovamente()
            break
        elif (rato == 1 and osso == 5 and gato == 7):
            borda('Parabéns. Passou de fase!!!')
            separaFase()
            quartaFase()
        break
def quartaFase():
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
            jogarNovamente()
            break
        else:
            borda('Parabéns. VocÊ Ganhou!!!')
            continuar = int(input(print('Deseja jogar novamente? 1 - SIM  0 - NÃO')))
            if (continuar == 0):
                break
            else:
                separaFase()
                primeiraFase()

# programa principal
while (cont ==1):
    primeiraFase()
        break