#Tabuada

n = int(input('Digite o valor que deseja calcular a tabuada: '))
x = int(input('Digite até qual número deseja mostrar a tabuada: '))
for t in range (1,x + 1,1): #x+1 pq o programa para em um numero antes.
    print('{} x {} = {}'.format(n,t,n*t))

print('-----------------------------------')
print('-----------------------------------')

tabuada = 1
while tabuada <= 10:
    print('-----------------------------------')
    print('TABUDA DO {}:'.format(tabuada))
    i=1
    while i <=10:
        print('{} x {} = {}'.format(tabuada, i, tabuada*i))
        i+=1 #i recebe i + 1
    tabuada +=1