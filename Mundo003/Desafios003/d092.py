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
previdencia['Nome: '] = str(input('Digite seu nome: '))
idade = date.today().year - (int(input('Digite seu ano de nascimento: ')))
previdencia['Idade: '] = idade
carteira = int(input('Carteira de Trabalho (0 não tem): '))
if carteira != 0:
    previdencia['CTPS: '] = carteira
previdencia['Contratação: '] = int(input('Digite o ano de contratação: '))
salario = float(input('Digite seu salário: '))
previdencia['Salário: '] = salario
aposentadoria = salario * (1 - 1.2)
previdencia['Aposentadoria: '] =