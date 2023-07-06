"""
Crie um programa que leia a idade e o sexo de várias
pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:

A) Quantas pessoas tem mais de 18 anos
B) Qunatos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos
"""

print(f'{" Desafio 069 ":=^30}')

m = h = m_m = 0
while True:
    n = str(input('Digite seu nome: '))
    i = int(input('Digite sua idade: '))
    s = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    if i > 18:
        m += 1
    if s == 'M':
        h += 1
    if s == 'F' and i < 20:
        m_m += 1
    print(f'''
Nome: {n}
Idade: {i}
Sexo: {'Feminino' if s == 'F' else 'Masculino'}''')
    d = str(input('Deseja continuar [S/N]?')).upper().strip()[0]
    if d != 'S':
        break

print(f'''
Maiores de 18: {m} pessoas
Homens cadastrados: {h} homens
Mulheres com menos de 20 anos: {m_m} mulheres''')