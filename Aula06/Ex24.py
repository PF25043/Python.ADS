#função
def buscaSequencial(lista,dados):
    x=0
    while x< len(lista):
        if (lista[x] ==dado):
            return x
        x += 1
    return -1
#programa principal
teste = [3,7,9,1,0,6,5,12]
dado=int(input('Digite um valor inteiro: '))
res = buscaSequencial(teste, dado)
if res>=0:
    print('Posição onde o {} foi encontrado: {}'.format(dado, res+1))
else:
    print('Dado não localizado...')
