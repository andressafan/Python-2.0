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
    nome = str(input('Cadastre um nome: '))
    sexo = str(input('Digite o sexo: ')).capitalize()
    idade = int(input('Digite a idade: '))
    nome = {'Nome': f'{nome}', 'Sexo': f'{sexo}', 'Idade': f'{idade}'}
    lista.append(nome.copy())
    d = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if d != 'S':
        print('Fim dos cadastros!')
        break

s_idade = 0
lista_mulheres = list()
idade_acima = list()
for i, e in enumerate(lista):
    s_idade += lista[i]['Idade']
    if lista[i]["Sexo"] == 'Feminino':
        lista_mulheres.append(lista[i]['Nome'])
media = s_idade / len(lista)
for i in lista:
    if lista[i]['Idade'] > media:
        idade_acima.append(lista[0]['Nome'])


print(f'''
Quantidade de pessoas cadastradas: {len(lista)}
Média da idade: {media}
Nomes das mulheres: {lista_mulheres}
Pessoas com idade acima da média: {idade_acima}
''')