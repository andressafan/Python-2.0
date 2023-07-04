# Escreva um programa que pergunte a quantidade de km
# percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço, sabendo que
# o carro custa R$60 por dia e R$0,15 por km rodado.

print('{:=^45}'.format('Desafio 015'))
km = float(input('Quantos quilômetros foram percorridos: '))
d = int(input('Por quantos dias o carro foi alugado: '))
p = (60 * d) + (km * 0.15)
print('Você pagará pelo aluguel o valor de: {:.2f} R$'.format(p))
