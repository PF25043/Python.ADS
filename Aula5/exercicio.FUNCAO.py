def validacao_string(nome, min, max):
    quant=len(nome)
    if ((quant<min)or (quant>max)):
        return False
    else:
        return True

nome = input('Digite um nome com até 10 letras:  ')
while validacao_string(nome,1,10):
    nome = input('Digite um nome com até 10 letras: ')
    print(nome)

print('###########################################')

#somar o intervalo entre 2 num.

#funções
def valida_int(pergunta, min, max):
    x=int(input(pergunta))
    while ((x<min) or (x>max)):
        x= int(input(pergunta))
    return x
def soma_intervalo(inicio, fim):
    soma = 0
    i = inicio
    while i<= fim:
        soma +=i
        i = i+1
    return soma
#programa principal:
x=valida_int('Digite um valor inteiro e positivo:', 1, 99999)
y=valida_int('Digite um segundo valor inteiro e positivo', 1, 99999)
print('Somatório entre {} e {} é {}.'.format(x,y, soma_intervalo(x,y)))
