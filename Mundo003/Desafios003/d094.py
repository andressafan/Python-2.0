"""
Crie um programa que leia nome, sexo e idade de várias pessoas
, guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média
"""

print(f'{" Desafio 094 ":=^50}')
lista = list()
while True:
    pessoa = {'Nome': str(input('Cadastre um nome: '))}
    while True:
        pessoa['Sexo'] = str(input('Digite o sexo: [M/F] ')).upper().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Erro! Digite um sexo válido!')
    pessoa['Idade'] = int(input('Digite a idade: '))
    lista.append(pessoa)
    d = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if d != 'S':
        print('Fim dos cadastros!')
        break

s_idade = 0
lista_mulheres = list()
idade_acima = list()
for pessoa in lista:
    s_idade += pessoa['Idade']
    if pessoa["Sexo"] in 'FEMININOF':
        lista_mulheres.append(pessoa['Nome'])

media = s_idade / len(lista)

for pessoa in lista:
    if pessoa['Idade'] > media:
        idade_acima.append(pessoa['Nome'])


print(f'''
Quantidade de pessoas cadastradas: {len(lista)}
Média da idade: {media}
Nomes das mulheres: {lista_mulheres}
Pessoas com idade acima da média: {idade_acima}
''')