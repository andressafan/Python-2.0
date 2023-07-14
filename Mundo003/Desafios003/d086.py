"""
Crie um programa que crie uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela com a formatação correta.
"""

print(f'{" Desafio 086 ":=^50}')

lista = [[], [], []]
#        [0] [1] [2]
#       [     0    ]
for e in range(3):  # e --> linhas
    for i in range(3):  # i --> colunas
        lista[e].insert(i, int(input(f'Digite um valor para {[e, i]}: ')))

print('='*50)

for e in range(3):
    print()
    for i in range(3):
        print(f"[{lista[e][i]:^3}]", end=' ')


