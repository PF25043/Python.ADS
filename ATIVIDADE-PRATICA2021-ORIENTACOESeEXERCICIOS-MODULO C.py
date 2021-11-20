#nome: Pâmela
#idade (RU): 28
nome= input('Nome da criança: ')
idade= int(input('Idade: '))
if(idade<=5):
    print('A aluna {} tem {} anos e está no Ensino Infantil.'.format(nome,idade))
elif(idade<=10):
    print('A aluna {} tem {} anos e está no Ensino Fundamental | .'.format(nome, idade))
elif(idade<=14):
    print('A aluna {} tem {} anos e está no Ensino Fundamental ||.'.format(nome, idade))
elif(idade>=15):
    print('A aluna {} tem {} anos e está no Ensino Médio.'.format(nome, idade))
cont= int(input('Deseja continuar?   0 - Não  1 - Sim  '))

x = cont
while(x==1):
    nome = input('Nome da criança: ')
    idade = int(input('Idade: '))
    if (idade <= 5):
        print('A aluna {} tem {} anos e está no Ensino Infantil.'.format(nome, idade))
    elif (idade <= 10):
        print('A aluna {} tem {} anos e está no Ensino Fundamental | .'.format(nome, idade))
    elif (idade <= 14):
        print('A aluna {} tem {} anos e está no Ensino Fundamental ||.'.format(nome, idade))
    elif (idade >= 15):
        print('A aluna {} tem {} anos e está no Ensino Médio.'.format(nome, idade))
    cont= int(input('Deseja continuar?   0 - Não  1 - Sim    '))
