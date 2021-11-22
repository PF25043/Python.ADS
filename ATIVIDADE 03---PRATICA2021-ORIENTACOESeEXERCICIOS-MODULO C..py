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

linha1=['*','*','*','*']
linha2=['*','*','*','*']
faze=1
contFase=0
continuar=1

#programa principal

#*********************************************** FASE 1
#***** Matriz fase 1
linha1[2]='_'
linha1[3]='G'
linha2[0]='R'
linha2[1]='_'
matrizF1a=(linha1)
matrizF1b=(linha2)

while (faze==1 and continuar==1 and continuar!=0):
    print('Bem vindo a faze 1!')
    print('Na fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que representa  os quartos:')
    print(matrizF1a)
    print(matrizF1b)
    rato= int(input(print('Em qual posição você que alocar o RATO? ')))
    while (rato!=3 and rato!=6):
            print('Quarto indisponível!')
            rato= int(input(print('Em qual posição você que alocar o RATO? ')))
    gato= int(input(print('Em qual posição você que alocar o GATO? ')))
    while (gato!=3 and gato!=6 or gato == rato):
            print('Quarto indisponível!')
            gato= int(input(print('Em qual posição você que alocar o GATO? ')))
    if(rato==3 and gato==6):
        print('Game Over!!!')
        print('Você perdeu...')
        continuar = int(input(print('Deseja jogar novamente? 1 - SIM  0 - NÃO')))
    elif(rato ==6 and gato==3):
        print('Parabéns. Você Ganhou!!!')
        contFase += 1

# ******************* Matriz fase 2
linha1[0]='_'
linha2[1]='C'
linha2[2]='_'
linha2[3]='_'
matrizF2a=(linha1)
matrizF2b=(linha2)
while (faze==2 and continuar==1 and continuar!=0):
print('Bem vindo a faze 2!')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print(matrizF2a)
print(matrizF2b)




