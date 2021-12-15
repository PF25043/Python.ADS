#função com mais de um parâmetro

#Função
def sub2(x,y):
    res = x-y
    print(res)

#Programa principal
sub2(10,5) #função de subtração
sub2(5,7)
sub2(1677,23)

print('|','___'*10,'|')
print('|','___'*10,'|')

#Função com parâmetro opcional
def soma(x=0,y=0,z=0): #atribuimos um valor à variàvel e assim caso ela fique de fora a função irá funcionar normalmente
    res = x+y+z
    print(res)

#Programa principal
soma(10,5) # só é possivel somar 2 nº ao inves de 3 pq atribuimos o valor zero às variàveis
soma(5,7,10)




