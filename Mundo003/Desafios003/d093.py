"""
Crie um programa que gerencie o aproveitamento de um jogador
de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos
em cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""


print(f'{" Desafio 093 ":=^50}')
aproveitamento = dict()
nome = str(input('Digite seu nome: '))
q = int(input('Quantidade de partidas: '))
s = 0
aproveitamento['Nome'] = nome
gols = list()
for i in range(q):
    gol = (int(input(f'Digite quantos gols fez na partida {i+1}: ')))
    gols.append(gol)
    s += gol
aproveitamento['Gols'] = gols
aproveitamento['Total'] = s
print(aproveitamento)
print('='*50)
for k, v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}')
print('='*50)
print(f'O jogador {aproveitamento["Nome"]} jogou {q} partidas.')
for i in range(len(gols)):
    print(f'Na partida {i + 1}, fez {gols[i]} ')
print(f'Foi um total de {s} gols')

