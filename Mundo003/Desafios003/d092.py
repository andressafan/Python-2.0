"""
Crie um programa que leia nome, ano de nascimento e carteira
de trabalho e cadastre-os (com idade) em um dicionário se por
acaso a CTPS for diferente de zero, o dicionário receberá
também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.
35 anos de colaboração
"""
print(f'{" Desafio 092 ":=^50}')
from datetime import date
previdencia = dict()
previdencia['Nome'] = str(input('Digite seu nome: '))
previdencia['Idade'] = date.today().year - (int(input('Digite seu ano de nascimento: ')))
previdencia['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if previdencia['CTPS'] != 0:
    previdencia['Contratação'] = int(input('Ano de Contratação: '))
    previdencia['Salário'] = float(input('Salário: R$ '))
    previdencia['Aposentadoria'] = previdencia['Idade'] + ((previdencia['Contratação'] + 35) - date.today().year)
print('='*50)
for k, v in previdencia.items():
    print(f'{k}: {v}')
