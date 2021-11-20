dnasc = int(input('Qual seu ano de nascimento? '))
anoat = int(input('Em que ano estamos? '))
idade = anoat - dnasc
print('Você tem {} anos de idade.'.format(idade))
if(idade >= 18):
    print('Você já maior de idade e já é possivel tirar a carteira de motorista!')