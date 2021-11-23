#Especificações
print(2*'\n')
print('*****************************')
print('*****************************')
print('    HOTEL DOS ANIMAIS')
print('*****************************')
print('*****************************')
print('\n')
print('Especificando posições:')
print('[1,2,3,4,]')
print('[5,6,7,8,]')
print('\n')
print('OBS: As posições com "*" já estão alocadas, escolha uma casa vazia "_"')
print('Regras do jogo:')
print('• O rato não pode ficar ao lado do gato')
print('• O cão não pode ficar ao lado do osso')
print('• O gato não pode ficar ao lado do cão')
print('• O queijo não pode ficar ao lado do rato')
print('\n')
print('Especificando das Letras:')
print('G – GATO')
print('C – CÃO')
print('R – RATO')
print('O – OSSO')
print('Q – QUEIJO')
print('\n')

#*******************************************

def separaFase(): #Separador de fases
    print('         |  |')
    print('         |  |')
    print('         |  |')
    print('         |  |')
    print('        \    /')
    print('         \  / ')
    print('          \/ ')

def borda(x): # borda utilizada quando o jogador acerta a fase
    tam = len(x)
    if tam:
        print('+', '-' * tam, '+')
        print('|', x, '|')
        print('+', '-' * tam, '+')

def matrizF1(): #Matriz das posições fase 1
    linha1 = ['*', '*', '_', 'G']
    linha2 = ['R', '_', '*', '*']
    matrizF1a = (linha1)
    matrizF1b = (linha2)
    print(matrizF1a)
    print(matrizF1b)

def matrizF2():#Matriz das posições fase 2
    linha1 = ['_', '*', '*', '*']
    linha2 = ['*', 'C', '_', '_']
    matrizF2a = (linha1)
    matrizF2b = (linha2)
    print(matrizF2a)
    print(matrizF2b)

def matrizF3():#Matriz das posições fase 3
    linha1 = ['_', '*', '*', '*']
    linha2 = ['_', 'G', '_', '*']
    matrizF3a = (linha1)
    matrizF3b = (linha2)
    print(matrizF3a)
    print(matrizF3b)

def matrizF4():#Matriz das posições fase 4
    linha1 = ['_', '_', '_', '*']
    linha2 = ['*', 'R', '*', '*']
    matrizF4a = (linha1)
    matrizF4b = (linha2)
    print(matrizF4a)
    print(matrizF4b)


# função fases

fase = 1 #variável de controle das fases
cont= 1 #variável de controle do andamento do jogo

def primeiraFase():
    global fase
    global cont
    if(fase==1):
        print('Bem vindo a fase 1!')
        print('Na fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que representa  os quartos:\n')
        matrizF1()
        rato = int(input(print('\nEm qual posição você quer alocar o RATO? ')))
        while (rato != 3 and rato != 6):
            print('Quarto indisponível!')
            rato = int(input(print('Em qual posição você quer alocar o RATO? ')))
        gato = int(input(print('Em qual posição você quer alocar o GATO? ')))
        while (gato != 3 and gato != 6 or gato == rato):
            print('Quarto indisponível!')
            gato = int(input(print('Em qual posição você quer alocar o GATO? ')))
        if (rato == 3 and gato == 6): #posição game over
            print('\n\nGame Over!!!')
            print('Você perdeu... \n\n')
            cont = int(input(print('Deseja jogar novamente? 1 - SIM  0 - NÃO')))
            if (cont == 1):
                    separaFase()
                    primeiraFase()
            elif (cont == 0):
                    print('Encerrando....')
        elif (rato == 6 and gato == 3): #posição correta
            borda('Parabéns. Passou de fase!!!')
            separaFase()
            fase = 2

def segundaFase():
    global fase
    global cont
    if(fase==2):
        print('\nBem vindo a fase 2!')
        print('Na segunda fase o jogador deve alocar : CÃO, CÃO E OSSO\n')
        matrizF2()
        caoA = int(input(print('\nEm qual posição você quer alocar o primeiro CÃO? ')))
        while (caoA != 1 and caoA != 7 and caoA != 8): #Posições inválidas para jogar
            print('Quarto indisponível!')
            caoA = int(input(print('Em qual posição você quer alocar o primeiro CÃO? ')))
        caoB = int(input(print('Em qual posição você quer alocar o segundo CÃO? ')))
        while (caoB != 1 and caoB != 7 and caoB != 8 or caoA == caoB): #Posições inválidas para jogar
            print('Quarto indisponível!')
            caoB = int(input(print('Em qual posição você quer alocar o segundo CÃO? ')))
        osso = int(input(print('Em qual posição você quer alocar o OSSO? ')))
        while (osso != 1 and osso != 7 and osso != 8 or osso == caoB or osso == caoA): #Posições inválidas para jogar
            print('Quarto indisponível!')
            osso = int(input(print('Em qual posição você quer alocar o OSSO? ')))
        if (osso != 1): #posição game over
            print('\n\nGame Over!!!')
            print('Você perdeu...\n\n')
            cont = int(input(print('Deseja jogar novamente? 1 - SIM  0 - NÃO')))
            if (cont == 1):
                separaFase()
                fase=1
                primeiraFase()
            elif (cont == 0):
                print('Encerrando....')
        else:
            borda('Parabéns. Passou de fase!!!')
            separaFase()
            fase=3

def terceiraFase():
    global fase
    global cont
    if(fase==3):
        print('Bem vindo a fase 3!')
        print('Na fase 3 o jogador deverá alocar : GATO, RATO E OSSO.\n')
        matrizF3()
        gato = int(input(print('\nEm qual posição você quer alocar o GATO? ')))
        while (gato != 1 and gato != 5 and gato != 7): #Posições inválidas para jogar
            print('Quarto indisponível!')
            gato = int(input(print('Em qual posição você quer alocar o GATO? ')))
        rato = int(input(print('Em qual posição você quer alocar o RATO? ')))
        while (rato != 1 and rato != 5 and rato != 7 or gato == rato): #Posições inválidas para jogar
            print('Quarto indisponível!')
            rato = int(input(print('Em qual posição você quer alocar o RATO? ')))
        osso = int(input(print('Em qual posição você quer alocar o OSSO? ')))
        while (osso != 1 and osso != 5 and osso != 7 or osso == rato or osso == gato): #Posições inválidas para jogar
            print('Quarto indisponível!')
            osso = int(input(print('Em qual posição você quer alocar o OSSO? ')))
        if (rato != 1 or osso != 5 or gato != 7): #posição game over
            print('\n\nGame Over!!!')
            print('Você perdeu... \n\n')
            cont = int(input(print('Deseja jogar novamente? 1 - SIM  0 - NÃO')))
            if (cont == 1):
                separaFase()
                fase = 1
                primeiraFase()
            elif (cont == 0):
                print('Encerrando....')
        elif (rato == 1 or osso == 5 or gato == 7): #posição correta
            borda('Parabéns. Passou de fase!!!')
            separaFase()
            fase = 4

def quartaFase():
    global fase
    global cont
    if(fase==4):
        print('Bem vindo a fase 4!')
        print('Na fase 4, o jogador deverá alocar: QUEIJO, QUEIJO, OSSO.\n')
        matrizF4()
        queijoA = int(input(print('\nEm qual posição você quer alocar o primeiro QUEIJO? ')))
        while (queijoA != 1 and queijoA != 2 and queijoA != 3): #Posições inválidas para jogar
            print('Quarto indisponível!')
            queijo = int(input(print('Em qual posição você quer alocar o primeiro QUEIJO? ')))
        queijoB = int(input(print('Em qual posição você quer alocar o segundo QUEIJO? ')))
        while (queijoB != 1 and queijoB != 2 and queijoB != 3 or queijoB == queijoA): #Posições inválidas para jogar
            print('Quarto indisponível!')
            queijoB = int(input(print('Em qual posição você quer alocar o segundo QUEIJO? ')))
        osso = int(input(print('Em qual posição você quer alocar o OSSO? ')))
        while (osso != 1 and osso != 2 and osso != 3 or osso == queijoB or osso == queijoA): #Posições inválidas para jogar
            print('Quarto indisponível!')
            osso = int(input(print('Em qual posição você quer alocar o OSSO? ')))
        if (osso != 2): #posição game over
            print('\n\nGame Over!!!')
            print('Você perdeu... \n\n')
        elif (osso == 2): #posição correta
            print(2 * '\n')
            borda('Parabéns. VocÊ Ganhou!!!')
            print(2 * '\n')
    cont = int(input(print('Deseja jogar novamente? 1 - SIM  0 - NÃO')))
    if (cont == 1):
        separaFase()
        fase = 1
        primeiraFase()
    elif (cont == 0):
        print('Encerrando....')
        cont=0


while cont==1:
    primeiraFase()
    segundaFase()
    terceiraFase()
    quartaFase()
