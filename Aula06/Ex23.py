try:
    notas = []
    x = float(input('Digite uma nota: '))
    while x>=0:
        notas.append(x)
        x = float(input('Digite uma nota: '))
    soma = 0
    for i in notas:
        soma +=i
    media= soma/len(notas)
    print (notas)
    print('Média das notas digitadas: {}'.format(media))
except ZeroDivisionError:
    print('Nenhum valor foi digitato para calcular. Encerrando...')

