def bordas(s1):
    tam = len(s1) #função para saber a quantidade de caractere de uma variavel
    if tam:
        print('+','-'* tam, '+')
        print('|',s1,'|')
        print('+', '-' * tam, '+')

bordas('olá, Mundo!')
bordas('Curso de lógica de programação de algorítmos')