"""
Crie um programa que leia nome e duas notas de vários
alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.
"""

print(f'{" Desafio 089 ":=^50}')
dados = list()
lista = list()
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite sua nota: ')))
    dados.append(float(input('Digite sua outra nota: ')))
    lista.append(dados[:])
    dados.clear()
    d = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if d != 'S':
        break

print('='*50)
print()
boletim = list()
m = 0
for notas in lista:
    m = (notas[1] + notas[2])/2
    print(f'{"Média do(a)" + f" {notas[0].capitalize()}" + " = " + f"{m}":^50}')



