"""
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O
programa será interrompido quando o número solicitado for
negativo.
"""

print(f'{" Desafio 067 ":=^30}')

n = c = 0
while True:
    n = int(input('Digite um número: '))
    c = 0
    if n <= 0:
        break
    while c <= 10:
        print(f'{n} x {c} = {n*c}')
        c += 1
