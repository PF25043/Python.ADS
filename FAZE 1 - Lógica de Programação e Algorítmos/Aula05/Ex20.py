def maior3(v1=0,v2=0, v3=0):
    if (v1 and v2 and v3):
        if(v1>v2) and (v1>v3):
            if(v2>v3):
                print('Ordem crescente: {},{},{}'.format(v3,v2,v1), end='')
            else:
                print('Ordem crescente: {},{},{}'.format(v2, v3, v1), end='')
        elif(v2>v1) and (v2>v3):
            if(v1>v3):
                print('Ordem crescente: {},{},{}'.format(v3, v1, v2), end='')
            else:
                print('Ordem crescente: {},{},{}'.format(v1, v3, v2), end='')
        elif(v3>v1) and (v3>v2):
            if(v1>v2):
                print('Ordem crescente: {},{},{}'.format(v2, v1, v3), end='')
            else:
                print('Ordem crescente: {},{},{}'.format(v2, v3, v1), end='')


x=int(input('Digite o primeiro valor:  '))
y=int(input('Digite o segundo valor:  '))
z=int(input('Digite o terceiro valor:  '))
maior3(x,y,z)
