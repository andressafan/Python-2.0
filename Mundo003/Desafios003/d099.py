"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer
qual deles é o maior.
"""

print(f'{" Desafio 099 ":=^50}')


def maior(numeros):  # --> recebe parâmetros da lista
    for i, n in enumerate(numeros):
        if i == 0:
            maior = n
        elif n > maior:
            maior = n
    print(f'Sua lista é {numeros}')
    print(f'O maior número é {maior}')


numeros = list()
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    d = str(input('Deseja parar? [S/N] ')).upper().strip()[0]
    if d == 'S':
        print('Guardando sua lista de números...')
        break

maior(numeros)
