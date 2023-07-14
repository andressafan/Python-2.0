"""
Faça um programa que leia o nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

"""


print(f'{" Desafio 084 ":=^50}')

dado = list()
cadastro = list()
lista_leves = list()
lista_pesadas = list()
c = 0
while True:
    dado.append(str(input('Digite seu nome: ')))
    dado.append(float(input('Digite seu peso: ')))
    cadastro.append(dado[:])
    dado.clear()
    c += 1
    d = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if d != 'S':
        print('Programa encerrado! ')
        break

for e in cadastro:
    if e[1] >= 100:
        lista_pesadas.append(e[0])
    elif e[1] <= 70:
        lista_leves.append(e[0])

print(f'''
Quantidade de cadastros: {c}
Pessoas com peso maior ou igual a 100: {lista_pesadas}
Pessoas com peso menor ou igual a 70: {lista_leves}
''')
