"""
Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado.
"""
print(f'{" Desafio 091 ":=^50}')
from random import randint
from operator import itemgetter
aposta = dict()
for i in range(4):
    jogador = f'Jogador {i+1}'
    valor = randint(1, 6)
    print(f'{jogador} tirou {valor}')
    aposta[jogador] = valor

print('='*50)
ranking = list()
for k, value in aposta.items():
    print(f'{k} tirou {value} no dado.')
ranking = sorted(aposta.items(), key=itemgetter(1), reverse=True)
# função itemgetter importada serve para pegar o item(1) (parte 1)
# do dicionário, ou seja em ordem de valor, se for (parte 0) ele coloca em ordem de chave
# e reverse para que fique em ordem decrescente do maior número ao menor.

print(f'{" Ranking dos Jogadores ":=^50}')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
