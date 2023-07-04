# Faça um algoritmo que leia o preço de um produto
# e mostre o seu novo preço, com 5% de desconto.

print('{:=^30}'.format('Desafio 012'))
p = float(input('Digite o preço do produto: R$ '))
d = p - (p * 0.05)
print('Seu produto no valor de {:.2f} R$'.format(p))
print('Sairá por {:.2f} R$'.format(d))
