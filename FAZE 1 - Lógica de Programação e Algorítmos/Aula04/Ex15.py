idade = int(input('Qual a sua idade? '))
while (idade>0):
    sexo = input ('Qual o seu sexo (M ou F)? ')
    if ((sexo == 'M') or (sexo == 'm')):
        print('Olá senhor, você possui {} anos'.format(idade))
    else:
        if ((sexo == 'F') or (sexo == 'f')):
            print('Olá senhora, você possui {} anos'.format(idade))
        else:
            print('Opção de sexo inválido.')
    idade = int(input('Qual a sua idade? '))
print('Encerrando...')
