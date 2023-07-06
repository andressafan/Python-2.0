"""
Crie um programa que leia o nome e o preço de vários produtos
. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$ 1000,00.
C) Qual é o nome do produto mais barato.
"""

print(f'{" Desafio 070 ":=^30}')

nome = ''
t = p_m = 0
p_b = float('inf')  # inicia a variável com um valor infinitamente alto
while True:
    n = str(input('Nome do produto: '))
    p = float(input('Preço do produto: '))
    t += p
    if p > 1000:
        p_m += 1

    if p < p_b:
        p_b = p
        nome = n

    d = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
    if d != 'S':
        print('Programa encerrado!')
        break

print(f'''
Total gasto: {t}
Produtos de mais de 1000,00 reais: {p_m}
Preço do produto mais barato: {p_b}
Nome do produto mais barato: {nome}''')


