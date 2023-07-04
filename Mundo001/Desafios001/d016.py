# Crie um programa que leia um número pelo teclado
# e mostre na tela a sua porção inteira.

"""import math
print('{:=^30}'.format('Desafio 016'))
n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(n, math.trunc(n)))"""

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
