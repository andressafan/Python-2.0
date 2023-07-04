# Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode comprar.

print('{:=^30}'.format('Desafio 010'))
print('{:-^30}'.format('Conversor de moedas'))
print('Cotação do Dólar: US$ 1,00 = R$ 3,27')
d = float(input('Digite o valor que você têm em reais: R$ '))
c = d / 3.27
print('Com {:.2f} R$\nVocê pode comprar {:.2f} dólares'.format(d, c))
