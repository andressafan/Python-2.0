"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.
"""

print(f'{" Desafio 090 ":=^50}')
boletim = dict()
boletim['Nome'] = str(input('Nome do aluno: '))
boletim['Média'] = float(input('Média do aluno: '))
boletim['Situação'] = 'Reprovado' if boletim['Média'] < 7 else 'Aprovado'
print('='*50)
for k, v in boletim.items():
    print(f'{k}: {v}')
print('='*50)


