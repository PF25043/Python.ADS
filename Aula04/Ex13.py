#VARREDUA DE STRING COM FOR

frase = 'Lógica de Programação e Algorítmos'
for x in range (0, len(frase),1):
# 0 ---> primeiro índice da variável inicia com zero
# len(frase) ---> len é o comando para informar a quantidade de índices que uma variável possui
# 1 ----> passo unitário
    #print(frase[x]) #para mostrar letra a letra uma abaixo da outra
    #print(x) #para mostrar o índice(numero) de casa catactere
    print(frase[x], end='') #para mostrar a frase em uma unica linha