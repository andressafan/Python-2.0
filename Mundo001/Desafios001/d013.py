# Faça um algoritmo que leia o salário de um
# funcionário e mostre o seu novo salário, com 15% de aumento.

print('{:=^30}'.format('Desafio 013'))
s = float(input('Digite o seu salário: R$ '))
a = s + (s * 0.15)
print('O seu salário receberá um aumento de {:.2f} R$'.format(s * 0.15))
print('Sairá de {:.2f} R$, para {:.2f} R$'.format(s, a))
