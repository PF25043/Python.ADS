x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))
cont = 1
mult = 0
while (cont <= x):
    mult = mult + y
    cont = cont + 1
print('Resultado da multiplicação: {} x {} = {}'.format(x,y,mult))
