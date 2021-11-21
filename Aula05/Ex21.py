#   RETORNO (em vez de aparecer na tela "print" a função retorno somente guarda o resultado "return")

def soma3(x=0 , y=0, z=0):
    resultado = x+y+z
    return resultado
#A variável resultado não esta no escopo gloal, desta forma, devemos criar uma variavel (com o mesmo nome ou não) no programa pricipal
resultado = soma3(3,2,1)
print(resultado)

# OU chamar pelo nome da função (forma mais simplificada abaixo):
print(soma3(1,2,3))

# Tambem é possivel armazenar varios resultados para imprimeir a soma somente no final... ex abaixo:

resultado1 = soma3(1,1,1)
resultado2 = soma3(2,2,2)
resultado3 = soma3(3,3,3)
print('somatório: {}, {} e {}.'.format(resultado1, resultado2, resultado3))

