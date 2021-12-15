#'a','@'
#'e','&'
#'i','!'
#'o','#'
#'u','*'


#programa principal
nome =input('Digite um nome: ') #Coletar o nome do usuário
nomeX=nome.upper() #Passar o nome para letras MAIÚSCULAS
nomeY=nomeX.replace('A','@').replace('E','&').replace('I','!').replace('O','#').replace('U','*') #Comando de substituição de string concatenado
print(nomeX) #print nome em MAIÚSCULO
print(nomeY) #print nome com os caracteres alterados









