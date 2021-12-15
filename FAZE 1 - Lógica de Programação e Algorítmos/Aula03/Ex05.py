salario = float(input('Qual o seu salário? '))
ano_adimissao = int(input('Em qual ano você foi admitido? '))
ano_atual = int(input('Em que ano estamos? '))
tempo = ano_atual - ano_adimissao
if(tempo >= 5):
    bonus = salario*0.2
    aumento = 20
else:
    bonus = salario * 0.1
    aumento = 10
print('Você possui {} anos de empresa e recebeu um almento de {}%.'.format(tempo,aumento))
print('Seu salário agora é de R${}.'.format(salario+bonus))