programa principal
nome =input('Digite um nome: ')
nomex=nome.upper()
nomey=nomex.replace('A,E,I,O,U', '@,&,!,#,*')
print(nomex)
print(nomey)

################################333

vogais={
    'a','@'
    'e','&'
    'i','!'
    'o','#'
    'u','*'
}
nome= input('Digite um nome: ')
nomeModificado=''

for i in nome():
    nomeModificado= nomeModificado+vogais[i]
print(nomeModificado)