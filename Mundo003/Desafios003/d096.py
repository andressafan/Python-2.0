"""
Faça um programa que tenha uma função chamada área(), que
receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno.
"""

print(f'{" Desafio 096 ":=^50}')
print(f'{" Controle de Terrenos ":=^50}')


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno com {larg} por {comp} é de {a}m²')


# Programa Principal
l = float(input('Largura do terreno (m): '))
c = float(input('Comprimento do terreno (m): '))
area(l, c)
