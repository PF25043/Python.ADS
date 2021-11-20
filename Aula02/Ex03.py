prod = float(input('Digite o valor do produto: '))
pct = int(input('Digite o percentual de desconto (0-100%): '))
des = prod / 100 * pct
vf = prod - des
print('O preço do produto é de {}. Desconto de {}%.'.format(prod, pct))
print('Valor calculado de desconto: R${}. Valor final do produto: R${}'.format(des, vf))