"""
Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
"""

print(f'{" Desafio 074 ":=^30}')
from random import randint

n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Valores sorteados: {n}')
menor = 999
maior = -999
for i in n:  # passa pelos elementos da tuplas
    # for i in (len(n)) # passa pelos índices dos elementos da tupla
    if i > maior:
        maior = i
        if maior > maior:
            maior = maior
    elif i < menor:
        menor = i
        if menor > menor:
            menor = menor

print(f'''
O menor número: {menor}
O maior número: {maior}''')

print(f'''
O menor número: {min(n)}
O maior número: {max(n)}''')
