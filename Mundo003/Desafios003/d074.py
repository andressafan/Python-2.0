"""
Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
"""

print(f'{" Desafio 074 ":=^30}')
import random

tupla = ()
for i in range(6):
    n = random.randint(1, 100)
    tupla = input(n)
print(tupla)
