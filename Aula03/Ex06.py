print('-------------------')
print('CALCULADORA')
print('-------------------')
print('+ Adição')
print('- Sutração')
print('* Multiplicação')
print('/ Divisão')
print('Precione outra tecla para sair')
print('-------------------')
operacao = input('Qual operação deseja realizar? ')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o seugndo valor: '))
if(operacao == '+'):
    res = n1+n2
elif(operacao == '-'):
    res = n1-n2
elif(operacao == '*'):
    res = n1*n2
elif(operacao == '/'):
    res = n1/n2
print('Resultado {} {} {} = {}'.format(n1,operacao,n2,res))