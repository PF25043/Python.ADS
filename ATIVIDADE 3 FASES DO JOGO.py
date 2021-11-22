linha1=['*','*','*','*']
linha2=['*','*','*','*']
fase=2
cont=1
#Codigo acima não precisa retornar para o arquivo pricipal

# ******************* Matriz fase 2
linha1[0]='_'
linha2[1]='C'
linha2[2]='_'
linha2[3]='_'
matrizF2a=(linha1)
matrizF2b=(linha2)

print('Bem vindo a faze 2!')
print('Na segunda fase o jogador deve alocar : CÃO, CÃO E OSSO')
print(matrizF2a)
print(matrizF2b)
caoA= int(input(print('Em qual posição você que alocar o primeiro CÃO? ')))
while (caoA != 1 and caoA != 7 and caoA != 8):
    print('Quarto indisponível!')
    caoA = int(input(print('Em qual posição você que alocar o primeiro CÃO? ')))
caoB= int(input(print('Em qual posição você que alocar o segundo CÃO? ')))
while (caoB != 1 and caoB != 7 and caoB != 8 or caoA==caoB):
    print('Quarto indisponível!')
    caoB = int(input(print('Em qual posição você que alocar o segundo CÃO? ')))
osso= int(input(print('Em qual posição você que alocar o OSSO? ')))
while (osso != 1 and osso != 7 and osso != 8 or osso==caoB or osso==caoA):
    print('Quarto indisponível!')
    osso= int(input(print('Em qual posição você que alocar o OSSO? ')))
if(osso!=1):
    print('Game Over!!!')
    print('Você perdeu...')
else:
    print('Parabéns. Você Ganhou!!!')
    fase = 3

fase=3
print('Bem vindo a faze 3!')