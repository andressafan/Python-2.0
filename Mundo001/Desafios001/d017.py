# Faça um programa que leia o comprimento
# do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.


import math
# from math import sqrt
print('{:=^30}'.format('Desafio 017'))
c_o = float(input('Digite o valor do cateto oposto: '))
c_a = float(input('Digite o valor do cateto adjacente: '))
# h = ((c_o ** 2 + c_a ** 2) ** 0.5)
# h = (c_o ** 2 + c_a ** 2) ** (1/2)
h = (c_o ** 2 + c_a ** 2)
print('O comprimento da hipotenusa será de: {}'.format(math.sqrt(h)))
