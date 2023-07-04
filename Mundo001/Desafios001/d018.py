# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente
# desse ângulo.

from math import sin, cos, tan, radians
print(f'{"Desafio 018":=^30}')
a = int(input('Digite o ângulo:'))
print('O valor do seno: {:.2f}'.format(sin(radians(a))))
print('O valor do cosseno: {:.2f}'.format(cos(radians(a))))
print('O valor da tangente: {:.2f}'.format(tan(radians(a))))
