#O programa deve receber apenas números inteiro e positivo até que o usuario digte zero.
#ao final, informar a média dos valores digitados.

soma = 0 #soma de todos os números inteiros
qnt = 0 #quantidade dos numeros inteiros digitados
x = 0 #numero digitado pelo usuário
while True:
    x = int(input('Digite um valor inteiro: '))
    if x < 0: #essa função irá ignorar numeros negativos
        continue #volta a linha 8 "Digite um valor inteiro: "
    if not x: #para o programa não para o not tranforma os valores int em false e o zero em true e o break para o loop
        break
    soma += x
    qnt += 1
media = soma / qnt
print('A média dos valores digitados é: {}'.format(media))